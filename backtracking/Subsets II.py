# Given an integer array nums that may contain duplicates, return all possible
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution in any order.

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        current_set:List[int] = []
        subsets:List[List[int]] = []

        self.generate_subsets(0, sorted(nums), current_set, subsets)

        print(subsets)
        return subsets

    def generate_subsets(self,i:int, nums:List[int], current_set:List[int], subsets:List[List[int]]):

        if i >= len(nums):
            subsets.append(current_set.copy())
            return

        current_set.append(nums[i])
        self.generate_subsets(i+1, nums, current_set, subsets)

        current_set.pop()

        while i + 1 < len(nums) and nums[i] == nums[i + 1]:
            i += 1
        self.generate_subsets(i + 1, nums, current_set, subsets)


nums = [1,2,2]

sol = Solution()
sol.subsetsWithDup(nums)
