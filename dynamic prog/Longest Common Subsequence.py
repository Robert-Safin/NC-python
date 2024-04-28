# Given two strings text1 and text2, return the length of their
# longest common subsequence. If there is no common subsequence, return 0.

# A subsequence of a string is a new string generated from the
# original string with some characters (can be none) deleted without
# changing the relative order of the remaining characters.

# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is
# common to both strings.

from collections import deque
from typing import Deque,List

def longestCommonSubsequence(text1: str, text2: str) -> int:
    # Initialize a grid with dimensions (len(text2) + 1) x (len(text1) + 1) for memoization
    grid = [[0] * (len(text1) + 1) for _ in range(len(text2) + 1)]

    # Start the DFS from the beginning of both texts
    return dfs(text1, text2, 0, 0, grid)

def dfs(text1: str, text2: str, r: int, c: int, grid: List[List[int]]):
    # Check if the end of either string has been reached
    if r == len(text2) or c == len(text1):
        return 0

    # Use memoized result if already computed
    if grid[r][c] != 0:
        return grid[r][c]

    # If the characters match, move diagonally in the grid
    if text1[c] == text2[r]:
        grid[r][c] = 1 + dfs(text1, text2, r + 1, c + 1, grid)
    else:
        # Otherwise, take the maximum of moving in one string or the other
        grid[r][c] = max(dfs(text1, text2, r + 1, c, grid), dfs(text1, text2, r, c + 1, grid))

    return grid[r][c]


text1 = "abcde"
text2 = "ace"

print(longestCommonSubsequence(text1,text2))
