# Given an array of integers nums, sort the array in ascending order
# and return it.

# You must solve the problem without using any built-in functions
# in O(nlog(n)) time complexity and with the smallest space complexity
# possible.

from typing import List




def sortArray(nums: List[int]) -> List[int]:
    # base case
    if len(nums) <= 1:
        return nums

    # get split index
    middle_index = len(nums) // 2

    # get splits
    left_split = nums[:middle_index]
    right_split = nums[middle_index:]

    # split splits
    left_sorted = sortArray(left_split)
    right_sorted = sortArray(right_split)

    # once splits are 1 element this triggers
    return merge(left_sorted, right_sorted)




def merge(left, right):
    result = []

    # check that splits are not empty before comparing them
    while (left and right):
        # compare values in splits, add to result and pop it
        if left[0] < right[0]:
            result.append(left[0])
            left.pop(0)
        else:
            result.append(right[0])
            right.pop(0)

    # if one split is empty, add the remainder of (sorted) split to result
    if left:
        result += left

    if right:
        result += right

    return result


sorted = sortArray([5,2,3,1])
print(sorted)
