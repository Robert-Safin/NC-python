# Given an integer array nums sorted in non-decreasing order, remove
# the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same. Then return
# the number of unique elements in nums.

from typing import List

def removeDuplicates(nums: List[int]) -> int:
    # Set left pointer to index 1 since we know the 1st element is always unique
    L = 1
    # Loop with right pointer excluding the 1st unique element
    for R in range(1, len(nums)):
        # Compare current value with previous value. Since array is sorted,
        # if the two values are different then we have found a new unique value
        # at right pointer.
        if nums[R] != nums[R - 1]:
            # update left pointer with new unique value
            nums[L] = nums[R]
            # bump left pointer
            L += 1
    # Modified array now has all the unique values in order at the beginning,
    # followed by duplicates
    print(nums)
    # Return number of unique elements
    return L



print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
