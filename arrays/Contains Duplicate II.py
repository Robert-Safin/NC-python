# Given an integer array nums and an integer k, return true if
# there are two distinct indices i and j in the array such
# that nums[i] == nums[j] and abs(i - j) <= k.

from typing import List,Set

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:

    window:Set[int] = set()

    for i in range(0, len(nums)):

        if nums[i] in window:
            return True

        window.add(nums[i])

        if len(window) > k:
            window.remove(nums[i - k])

    return False



nums = [1,2,3,1]
k = 3

print(containsNearbyDuplicate(nums, k)) # true
