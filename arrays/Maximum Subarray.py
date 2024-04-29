# Given an integer array nums, find the subarray with the largest sum,
# and return its sum in N(0).

from typing import List

def maxSubArray(nums: List[int]) -> int:

    # return var, assign to [0] handles 1 len arrays
    max_sum:int = nums[0]
    # greedy sum
    curr_sum:int = 0



    for n in nums:
        # greedy part: reset curr_sum if its negative
        curr_sum = max(curr_sum, 0)
        # build current sum
        curr_sum += n
        # reassign max_sum if better slice is found
        max_sum = max(curr_sum, max_sum)

    return max_sum




nums = [-2,1,-3,4,-1,2,1,-5,4] # 6
print(maxSubArray(nums))


nums = [-1] # -1
print(maxSubArray(nums))
