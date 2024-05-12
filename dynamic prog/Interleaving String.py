# Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

# An interleaving of two strings s and t is a configuration where s and t are divided into n and m
# substrings
#  respectively, such that:


from typing import Dict,List,Tuple

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        return self.dfs(s1, s2, s3, 0, 0, 0, {})

    def dfs(self, s1:str ,s2:str, s3:str, i1: int, i2: int, i3:int, cache:Dict[Tuple[int,int],bool]) -> bool:

        if (i1, i2) in cache:
            return cache[(i1, i2)]

        if i1 == len(s1) and i2 == len(s2):
            return True

        if i3 == len(s3):
            return False

        res = False
        if i1 < len(s1) and s1[i1] == s3[i3]:
            if self.dfs(s1,s2,s3, i1 + 1, i2, i3 + 1, cache):
                res = True

        if i2 < len(s2) and s2[i2] == s3[i3]:
            if self.dfs(s1,s2,s3, i1, i2 + 1, i3 + 1, cache):
                res = True

        cache[(i1, i2)] = res
        return res






sol = Solution()

# s1 = "aabcc"
# s2 = "dbbca"
# s3 = "aadbbcbcac"
# print(sol.isInterleave(s1,s2,s3)) # True

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


# s1 ="bbbbbabbbbabaababaaaabbababbaaabbabbaaabaaaaababbbababbbbbabbbbababbabaabababbbaabababababbbaaababaa"
# s2 ="babaaaabbababbbabbbbaabaabbaabbbbaabaaabaababaaaabaaabbaaabaaaabaabaabbbbbbbbbbbabaaabbababbabbabaab"
# s3 ="babbbabbbaaabbababbbbababaabbabaabaaabbbbabbbaaabbbaaaaabbbbaabbaaabababbaaaaaabababbababaababbababbbababbbbaaaabaabbabbaaaaabbabbaaaabbbaabaaabaababaababbaaabbbbbabbbbaabbabaabbbbabaaabbababbabbabbab"
# print(sol.isInterleave(s1,s2,s3)) # false


# s1 = ""
# s2 = ""
# s3 = "a"
# print(sol.isInterleave(s1,s2,s3)) # false


s1 = "a"
s2 = "b"
s3 = "a"
print(sol.isInterleave(s1,s2,s3)) # false
