# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations:List[List[int]] = []

        self.generate_combinations(n,k,combinations,[],1)

        return combinations

    def generate_combinations(self, n: int, k: int, combinations:List[List[int]], current_combination:List[int], i:int):

        if len(current_combination) == k:
            combinations.append(current_combination.copy())
            return
        if i > n:
            return
        # decision to include i
        current_combination.append(i)
        self.generate_combinations(n, k, combinations, current_combination,i+1)
        current_combination.pop()

        # decision to NOT include i
        self.generate_combinations(n, k, combinations, current_combination,i+1)



sol = Solution()
n = 4
k = 2

sol.combine(n,k)
