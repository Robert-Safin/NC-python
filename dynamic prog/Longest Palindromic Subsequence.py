# Given a string s, find the longest palindromic subsequence's length in s.

# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.




class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # Create a 2D table to store the lengths of longest palindromic subsequences
        dp = [[0] * n for _ in range(n)]

        # Initialize diagonal elements to 1 (each character is a palindrome of length 1)
        for i in range(n):
            dp[i][i] = 1

        # Fill the table diagonally
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # The longest palindromic subsequence length is at the top-right corner of the table
        return dp[0][n - 1]




















# from typing import Tuple, Dict

# class Solution:
#     def longestPalindromeSubseq(self, s: str) -> int:

#         longest = 0

#         for i in range(len(s)):
#             left = i
#             right = i

#             odd = self.dfs(s,left,right, {})
#             if odd > longest:
#                 longest = odd

#             even = self.dfs(s,left,right+1, {})
#             if even > longest:
#                 longest = even

#         return longest

#     def dfs(self, s:str, left:int, right:int, cache:Dict[Tuple[int,int],int]) -> int:

#         if left < 0 or right >= len(s):
#             return 0

#         if (left,right) in cache:
#             return cache[(left,right)]

#         if s[left] == s[right] and left != right:
#             cache[(left,right)] = 2 + self.dfs(s,left-1,right+1, cache)

#         elif s[left] == s[right] and left == right:
#             cache[(left,right)] = 1 + self.dfs(s,left-1,right+1, cache)

#         else:
#             cache[(left,right)] =  max(self.dfs(s,left-1,right, cache), self.dfs(s,left,right+1, cache))

#         return cache[(left,right)]












sol = Solution()



s = "bbbab"
print(sol.longestPalindromeSubseq(s)) # 4



# s = "cbbd"
# print(sol.longestPalindromeSubseq(s)) # 2


# s = "aabaa"
# print(sol.longestPalindromeSubseq(s)) # 5


# s = "euazbipzncptldueeuechubrcourfpftcebikrxhybkymimgvldiwqvkszfycvqyvtiwfckexmowcxztkfyzqovbtmzpxojfofbvwnncajvrvdbvjhcrameamcfmcoxryjukhpljwszknhiypvyskmsujkuggpztltpgoczafmfelahqwjbhxtjmebnymdyxoeodqmvkxittxjnlltmoobsgzdfhismogqfpfhvqnxeuosjqqalvwhsidgiavcatjjgeztrjuoixxxoznklcxolgpuktirmduxdywwlbikaqkqajzbsjvdgjcnbtfksqhquiwnwflkldgdrqrnwmshdpykicozfowmumzeuznolmgjlltypyufpzjpuvucmesnnrwppheizkapovoloneaxpfinaontwtdqsdvzmqlgkdxlbeguackbdkftzbnynmcejtwudocemcfnuzbttcoew"
# print(sol.longestPalindromeSubseq(s))
