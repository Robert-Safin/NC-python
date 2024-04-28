from typing import List

def maxIslandArea(grid: List[List[str]]) -> int:
    if not grid:
        return 0

    areas:List[int] = []

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if grid[row][col] == '1':

                area = dfs(grid, row, col)
                areas.append(area)
    print(areas)
    return max(areas)

def dfs(grid: List[List[str]], r: int, c: int) -> int:

    if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] == '0':
        return 0


    grid[r][c] = '0'


    area = 1

    area += dfs(grid, r + 1, c)
    area += dfs(grid, r - 1, c)
    area += dfs(grid, r, c + 1)
    area += dfs(grid, r, c - 1)

    return area


grid = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
] # should be 3

print(maxIslandArea(grid))
