# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

from typing import List

def findDuplicate(nums: List[int]) -> int:
    # this is a technically a linked list cycle problem.
    # as array distinct values in range (1 => N) but length N+1
    # we can use the array values to index into next value (like linked list)
    slow = 0
    fast = 0
    slow2 = 0

    # problem guarantees there is a duplicate value (cycle) so can use endless loop
    while True:
        # bump slow once
        slow = nums[slow]

        # bump fast twice
        fast = nums[fast]
        fast = nums[fast]

        # detect cycle
        if slow == fast:
            # begin moving slow2 pointer
            while slow != slow2:
                slow = nums[slow]
                slow2 = nums[slow2]
            # return inception value
            return slow2



nums = [1,3,4,2,2]
findDuplicate(nums) # 2
