# Given an integer array nums, handle multiple queries of the following type:

# Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
# Implement the NumArray class:

# NumArray(int[] nums) Initializes the object with the integer array nums.
# int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).




from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        vals = []
        sum = 0
        for i in nums:
            sum += i
            vals.append(sum)
        self.vals = vals

    def sumRange(self, left: int, right: int) -> int:
        # handle edge case of left == 0
        left_bound = 0
        if left > 0:
            left_bound = self.vals[left - 1]

        return self.vals[right] - left_bound


nr = NumArray([-2, 0, 3, -5, 2, -1])

print(nr.sumRange(0,2)) # 1
print(nr.sumRange(2,5)) # -1
print(nr.sumRange(0,5)) # -3
