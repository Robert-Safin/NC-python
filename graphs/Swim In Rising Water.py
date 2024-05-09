# You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point (i, j).

# The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t. You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during your swim.

# Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left square (0, 0).
from typing import List
import heapq
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        t = 0

        while True:
            t+=1
            if self.can_reach_end(grid,t):

                if t == 0:
                    return 1
                else:
                    return t



    def can_reach_end(self, grid:List[List[int]], t:int) -> bool:
        ROWS = len(grid)
        COLS = len(grid[0])
        END = grid[len(grid)-1][len(grid[0])-1]

        if grid[0][0] > t:
            return False


        min_heap = [(grid[0][0],0,0)]
        shortest_paths = {}

        while min_heap:
            elevation, row_i, col_i = heapq.heappop(min_heap)

            if elevation in shortest_paths:
                continue

            shortest_paths[elevation] = elevation

            if END in shortest_paths:
                return True

            neighbors = [   [row_i+1,col_i],
                            [row_i,col_i+1],
                            [row_i-1,col_i],
                            [row_i,col_i-1]    ]

            for neighbor_row, neighbor_col in neighbors:
                if (0 <= neighbor_row < ROWS and 0 <= neighbor_col < COLS and
                    grid[neighbor_row][neighbor_col] <= t and
                    grid[neighbor_row][neighbor_col] not in shortest_paths):

                    heapq.heappush(min_heap, (grid[neighbor_row][neighbor_col], neighbor_row, neighbor_col))

        return False



sol = Solution()
grid = [[0,2],
        [1,3]]
sol.swimInWater(grid) # 3


grid = [[3,2],
        [0,1]] # 3
sol.swimInWater(grid)
