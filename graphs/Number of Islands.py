# Given an m x n 2D binary grid grid which represents a map of
# '1's (land) and '0's (water), return the number of islands.

# An island is surrounded by water and is formed by connecting adjacent
# lands horizontally or vertically. You may assume all four edges of the
# grid are all surrounded by water.

from typing import List,Tuple,Set

def numIslands(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    island_count = 0

    for row_i, row in enumerate(grid):
        for col_i, cell_v in enumerate(row):
            if cell_v == '1':
                island_count += 1
                dfs(grid,row_i,col_i)

    return island_count



def dfs(grid:List[List[str]], r:int, c:int):
    n_of_rows = len(grid)
    n_of_cols = len(grid[0])

    if (r < 0 or c < 0 or
        r == n_of_rows or c == n_of_cols or
        grid[r][c] == '0'
        ):
        return
    else:
        grid[r][c] = '0'
        dfs(grid,r + 1, c)  # Visit down
        dfs(grid,r - 1, c)  # Visit up
        dfs(grid,r, c + 1)  # Visit right
        dfs(grid,r, c - 1)  # Visit left








grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
] # should be 3

print(numIslands(grid))
