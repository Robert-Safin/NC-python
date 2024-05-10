# You are given an integer array nums and an integer target.

# You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

# For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
# Return the number of different expressions that you can build, which evaluates to target.
from typing import List,Dict,Tuple
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        return self.dfs(0,nums,target,0,0,{})

    def dfs(self, i:int, nums:List[int], target:int, count:int, current_sum:int, cache:Dict[Tuple[int,int],int]) -> int:

        # can only check sum when all numbers have been used
        if i == len(nums):
            # yes
            if current_sum == target:
                return 1
            # no
            return 0

        # all below runs until base case is reached
        # check cache
        if (i,current_sum) in cache:
            return cache[(i,current_sum)]

        # update count
        count += self.dfs(i+1,nums,target,count,current_sum+nums[i],cache) + self.dfs(i+1,nums,target,count,current_sum-nums[i],cache)
        # update cache
        cache[(i,current_sum)] = count
        return count



sol = Solution()
nums = [1,1,1,1,1]
target = 3

print(sol.findTargetSumWays(nums, target)) # 5
