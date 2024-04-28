


from typing import List

def uniquePathsWithObstacles(obstacleGrid: List[List[int]]) -> int:
    cache:List[List[int]] = [ [ 0 for _ in range(len(obstacleGrid[0])) ] for _ in range(len(obstacleGrid)) ]

    return move(obstacleGrid, 0, 0, cache)


def move(grid:List[List[int]], row:int, col:int, cache):

    if row == len(grid) or col == len(grid[0]):
        return 0

    if grid[row][col] == 1:
        return 0

    if cache[row][col] != 0:
        return cache[row][col]

    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        return 1

    cache[row][col] = move(grid,row + 1,col, cache) + move(grid,row,col + 1, cache)

    return cache[row][col]



grid = [[0,0,0],[0,1,0],[0,0,0]]
print(uniquePathsWithObstacles(grid))
