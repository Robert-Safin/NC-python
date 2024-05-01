# Given an integer array nums sorted in non-decreasing order, remove some
# duplicates in-place such that each unique element appears at most twice.
# The relative order of the elements should be kept the same.

# Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates,
# then the first k elements of nums should hold the final result.
# It does not matter what you leave beyond the first k elements.

# Return k after placing the final result in the first k slots of nums.

# Do not allocate extra space for another array. You must do this by modifying
# the input array in-place with O(1) extra memory.

from typing import List

def removeDuplicates(nums: List[int]) -> int:

    # lags behind staying at index of value which needs to be replaces
    LEFT = 0
    # scans forward for sequences
    RIGHT = 0

    while RIGHT < len(nums):

        # count repeating sequence
        sequence_count = 1

        # FIRST check if right+1 is valid index
        # SECOND check continuation of sequence
        while RIGHT + 1 < len(nums) and nums[RIGHT] == nums[RIGHT + 1]:
            sequence_count += 1
            RIGHT += 1

        # handle variety of sequence lengths but constrain to max of 2
        for _ in range(min (2, sequence_count)):
            # update left value with right value
            nums[LEFT] = nums[RIGHT]
            # shift left into next index
            LEFT += 1

        # bump right onto the beginning of next sequence
        # the outer while will prevent from indexing out of bounds
        RIGHT += 1

    # slice [:LEFT] is length of valid array
    return LEFT





nums = [1,1,1,2,2,3]
#Output: 5, nums = [1,1,2,2,3,_]
print(removeDuplicates(nums))

#nums = [0,0,1,1,1,1,2,3,3]
#Output: 7, nums = [0,0,1,1,2,3,3,_,_]
#print(removeDuplicates(nums))
