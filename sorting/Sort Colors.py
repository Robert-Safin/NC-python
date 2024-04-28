# Given an array nums with n objects colored red, white, or blue,
# sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white, and blue.

# We will use the integers 0, 1, and 2 to represent the color red, white,
# and blue, respectively.

# You must solve this problem without using the library's sort function.

from typing import List
# bucket sort
def sortColors(nums: List[int]) -> None:
    # since there are 3 possible values in nums
    counts = [0,0,0]

    # count occurrences
    for i in nums:
        counts[i] += 1

    # track the position in the original array
    pointer = 0

    # counts indices - also value at index
    for n in range(0,len(counts)):
        # count[index] times update original array with count[index] value
        # bump pointer
        for _ in range(0,counts[n]):
            nums[pointer] = n
            pointer += 1







nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
sortColors(nums)
print(nums)
