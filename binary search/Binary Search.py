# Given an array of integers nums which is sorted in ascending order,
# and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.
from typing import List


def search(nums: List[int], target: int) -> int:
    # init left and right INDEX pointers, hence right is -1 from length
    left = 0
    right = len(nums) - 1

    # handles case where target is not in nums.
    while left <= right:
        # calc mid index
        mid = (right + left) // 2
        # target is on the left, reassign right
        if nums[mid] > target:
            right = mid - 1
        # target is on the right, reassign left
        elif nums[mid] < target:
            left = mid + 1
        else:
        # mid == target
            return mid

    # target not in nums
    return -1




nums = [1,2,3,5,9,12]
target = 9

index = search(nums,target) # 4
print(index)
