# Given an array of distinct integers candidates and a target integer target,
# return a list of all unique combinations of candidates where the chosen
# numbers sum to target. You may return the combinations in any order.

# The same number may be chosen from candidates an unlimited number of times.
# Two combinations are unique if the
# frequency
#  of at least one of the chosen numbers is different.

# The test cases are generated such that the number of unique combinations
# that sum up to target is less than 150 combinations for the given input.

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        combinations:List[List[int]] = []
        self.generate_combinations(0, candidates, target, [],combinations)
        print(combinations)
        return combinations

    def generate_combinations(self, i:int, candidates: List[int], target: int, current_combination:List[int], combinations:List[List[int]]):

        if i >= len(candidates):
            return

        if sum(current_combination) == target:
            combinations.append(current_combination.copy())
            return

        if sum(current_combination) > target:
            return


        current_combination.append(candidates[i])
        self.generate_combinations(i, candidates, target, current_combination.copy(), combinations)
        current_combination.pop()

        self.generate_combinations(i + 1, candidates, target, current_combination.copy(), combinations)

sol = Solution()
candidates = [2,3,6,7]
target = 7
sol.combinationSum(candidates,target)
