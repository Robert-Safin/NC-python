# Given two strings text1 and text2, return the length of their
# longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the
# original string with some characters (can be none) deleted without
# changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is
# common to both strings.


from typing import Dict,Tuple


# bottom-up
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        ROWS = len(text1)
        COLS = len(text2)

        grid = [ [0 for _ in range(COLS+1) ] for _ in range(ROWS+1) ]

        for row in range(ROWS):
            for col in range(COLS):

                if text1[row] == text2[col]:
                    grid[row+1][col+1] = 1 + grid[row][col]
                else:
                    grid[row+1][col+1] = max(grid[row][col+1], grid[row+1][col])

        return grid[ROWS][COLS]






# # top-down
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:

#         return self.dfs(text1, text2, 0,0, {})

#     def dfs(self, text1:str, text2:str, i1:int, i2:int, cache:Dict[Tuple[int,int],int]) -> int:

#         if i1 == len(text1) or i2 == len(text2):
#             return 0

#         if (i1,i2) in cache:
#             return cache[(i1,i2)]

#         if text1[i1] == text2[i2]:
#             return 1 + self.dfs(text1, text2, i1+1, i2+1, cache)

#         cache[(i1,i2)] =  max(
#             self.dfs(text1, text2, i1+1, i2, cache),
#             self.dfs(text1, text2, i1, i2+1, cache)
#         )

#         return cache[(i1,i2)]






sol = Solution()
text1 = "abcde"
text2 = "ace"

print(sol.longestCommonSubsequence(text1,text2)) # 3
