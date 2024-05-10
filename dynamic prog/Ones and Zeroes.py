# You are given an array of binary strings strs and two integers m and n.

# Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

# A set x is a subset of a set y if all elements of x are also elements of y.


from typing import List, Dict, Tuple

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:

        return self.dfs(0,m,n, {}, strs)



    def dfs(self,i:int, m:int, n:int, dp, strs:List[str]):

        if i == len(strs):
            return 0

        if (i, m, n) in dp:
            return dp[(i, m, n)]

        zero_count = strs[i].count("0")
        one_count = strs[i].count("1")

        dp[(i, m, n)] = self.dfs(i + 1, m, n, dp,strs)

        if zero_count <= m and one_count <= n:
            dp[(i, m, n)] = max(
                dp[(i, m, n)],
                1 + self.dfs(i + 1, m - zero_count, n - one_count, dp,strs))

        return dp[(i, m, n)]



sol = Solution()
strs = ["10","0001","111001","1","0"]
m = 5
n = 3
print(sol.findMaxForm(strs,m,n)) # 4
