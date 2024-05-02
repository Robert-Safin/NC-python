# Given an array of integers nums, calculate the pivot index of this array.

# The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

# If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

# Return the leftmost pivot index. If no such index exists, return -1.

from typing import List

def pivotIndex(nums: List[int]) -> int:
    # init sums at both ends
    right_sum = sum(nums)
    left_sum = 0

    for i in range(len(nums)):
        # update left OR right sum, order doesn't matter
        left_sum += nums[i]

        # between sum updates, check for a match
        if left_sum == right_sum:
            return i

        # update other sum
        right_sum -= nums[i]


    return -1


nums = [1,7,3,6,5,6]
#      [1,8,11,*,11,6]
print(pivotIndex(nums)) # 3
