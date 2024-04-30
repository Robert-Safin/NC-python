# Given an array of positive integers nums and a positive integer target,
# return the minimal length of a subarray whose sum is greater than
# or equal to target. If there is no such subarray, return 0 instead.

from typing import List

def minSubArrayLen(target: int, nums: List[int]) -> int:

    # trailing pointer
    LEFT = 0
    running_sum = 0
    min_length = 999999

    # Right pointer keeps running until it hits the while check
    for RIGHT in range(len(nums)):

        # add num to running_sum
        running_sum += nums[RIGHT]

        # if running_sum is < target this won't run.
        # once is true, start popping tail number via left pointer
        # stops popping when running_sum is < target
        while running_sum >= target:
            min_length = min(RIGHT - LEFT + 1, min_length)
            running_sum -= nums[LEFT]
            # no reset of left pointer as logically impossible
            # to find valid slices by going back,
            LEFT += 1

    return 0 if min_length == 999999 else min_length





target = 7
nums = [2,3,1,2,4,3]


print(minSubArrayLen(target, nums)) # 2
