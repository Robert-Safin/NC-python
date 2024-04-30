# Given a 1-indexed array of integers numbers that is already sorted
# in non-decreasing order, find two numbers such that they add up to a
# specific target number. Let these two numbers be numbers[index1]
# and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by
# one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution.
# You may not use the same element twice.

# Your solution must use only constant extra space.

from typing import List

# {{{[[ 1-INDEXED ARRAY??? ]]}}}
def twoSum(numbers: List[int], target: int) -> List[int]:

    # pointer at smallest and largest vals in sorted array
    LEFT = 0
    RIGHT = len(numbers) - 1

    while LEFT < RIGHT:
        sum = numbers[LEFT] + numbers[RIGHT]

        # target can never be reached with the smallest value, take one bigger
        if sum < target:
            LEFT += 1
        # target can never be reached with the largest value, take one smaller
        elif sum > target:
            RIGHT -= 1
        else:
            return [LEFT + 1 , RIGHT + 1]

    return []




numbers = [2,7,11,15]
target = 9
print(twoSum(numbers,target)) # [1,2]


numbers = [2,3,4]
target = 6
print(twoSum(numbers,target)) # [1,3]
