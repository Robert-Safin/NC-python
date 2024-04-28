# There is a robot on an m x n grid. The robot is initially
# located at the top-left corner (i.e., grid[0][0]). The robot
# tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]).
# The robot can only move either down or right at any point in time.

# Given the two integers m and n, return the number of possible unique
# paths that the robot can take to reach the bottom-right corner.

# The test cases are generated so that the answer will be less than or
# equal to 2 * 109.

from typing import List

def uniquePaths(m: int, n: int):
    cache:List[List[int]] = [ [ 0 for _ in range(n) ] for _ in range(m) ]


    return brute(m, n, 0, 0, cache)


def brute(m: int, n: int, row_i:int, col_i:int, cache):

    if row_i == m or col_i == n:
        return 0

    if cache[row_i][col_i] != 0:
        return cache[row_i][col_i]

    if row_i == m - 1 and col_i == n - 1:
        return 1

    cache[row_i][col_i] = brute(m,n,row_i + 1,col_i, cache) + brute(m,n,row_i,col_i + 1, cache)

    return cache[row_i][col_i]



print(uniquePaths(4,4))
