# Given an integer array nums and an integer val, remove all occurrences of val
# in nums in-place. The order of the elements may be changed. Then return the
# number of elements in nums which are not equal to val.
from typing import List

def removeElement(nums: List[int], val: int) -> int:
    # Non val counter
    k = 0
    # Loop through entire array
    for i in range(0,len(nums)):
        # If val is found, run nested loop looking for non val to swap with
        if nums[i] == val:
            for y in range(i+1,len(nums)):
                if nums[y] != val:
                    nums[i], nums[y] = nums[y], nums[i]
                    # Bump counter as we have swapped val with non val, break inner loop
                    k += 1
                    break
        else:
            # Bump counter as we have passed a non val
            k += 1
    # All vals have been bubbled to the end of the array
    print(nums)
    # Number of non val values
    print(k)
    return k

removeElement([0,1,2,2,3,0,4,2],2)
