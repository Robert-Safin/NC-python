# Given an integer array nums, return true if you can partition the array
# into two subsets such that the sum of the elements in both subsets
# is equal or false otherwise.
from typing import List,Dict,Tuple



class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums) / 2
        return self.dfs(nums, target, 0, 0, {})

    def dfs(self, nums: List[int], target: float, i: int, current_sum: int, cache: Dict[Tuple[int,int], bool]) -> bool:
        # Check if the result for the current subproblem is already cached
        if (i, current_sum) in cache:
            return cache[(i, current_sum)]

        if current_sum == target:
            cache[(i, current_sum)] = True
            return True

        if current_sum > target or i == len(nums):
            cache[(i, current_sum)] = False
            return False

        # Include the current number in the subset
        if self.dfs(nums, target, i + 1, current_sum + nums[i], cache):
            cache[(i, current_sum)] = True
            return True

        # Exclude the current number from the subset
        if self.dfs(nums, target, i + 1, current_sum, cache):
            cache[(i, current_sum)] = True
            return True

        cache[(i, current_sum)] = False
        return False




sol = Solution()

# nums = [1,5,11,5]
# print(sol.canPartition(nums)) # true

nums = [100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,99,97]
print(sol.canPartition(nums)) # False
# nums = [1,2,3,5]
# print(sol.canPartition(nums)) # false
