# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

# An interleaving of two strings s and t is a configuration where s and t are divided into n and m
# substrings
#  respectively, such that:


from typing import Dict,List,Tuple

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        return True

    def dfs(self, s1: str, s2: str, s3: str, i1:int, i2:int, i3:int) -> bool:

        return True


sol = Solution()

s1 = "aabcc"
s2 = "dbbca"
s3 = "aadbbcbcac"
print(sol.isInterleave(s1,s2,s3)) # True

# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbbaccc"
# print(sol.isInterleave(s1,s2,s3)) # False

# s1 = ""
# s2 = ""
# s3 = ""
# print(sol.isInterleave(s1,s2,s3)) # True


# s1 = "aabd"
# s2 = "abdc"
# s3 = "aabdbadc"
# print(sol.isInterleave(s1,s2,s3)) # false
