# Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

# You have the following three operations permitted on a word:

# Insert a character
# Delete a character
# Replace a character



from typing import Dict,Tuple

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        return self.dfs(word1, word2, 0, 0, {})

    def dfs(self, word1: str, word2: str, i1:int, i2:int, cache:Dict[Tuple[int,int],int]) -> int:

        if (i1,i2) in cache:
            return cache[(i1,i2)]


        # base case if index out of bounds return the remaining length
        if i1 == len(word1):
            return len(word2) - i2
        if i2 == len(word2):
            return len(word1) - i1

        # if the characters are equal we can skip them
        if word1[i1] == word2[i2]:
            return self.dfs(word1, word2, i1+1, i2+1, cache)

        # if the characters are not equal we have 3 options
        # brute force all 3 options and return the minimum
        cache[(i1,i2)] = min(
        1 + self.dfs(word1, word2, i1, i2+1, cache),
        1 + self.dfs(word1, word2, i1+1, i2, cache),
        1 + self.dfs(word1, word2, i1+1, i2+1, cache),
        )

        return cache[(i1,i2)]




sol = Solution()

word1 = "horse"
word2 = "ros"
print(sol.minDistance(word1,word2)) # 3


# word1 = "intention"
# word2 = "execution"
# print(sol.minDistance(word1,word2)) # 5
