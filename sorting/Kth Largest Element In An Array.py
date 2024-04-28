# Given an integer array nums and an integer k, return the kth largest
# element in the array.

# Note that it is the kth largest element in the sorted order,
# not the kth distinct element.

# Can you solve it without sorting?

# quick sort
from typing import List

def findKthLargest(nums: List[int], k: int) -> int:
    # edge case
    if not nums:
        return -1

    # select a pivot
    pivot_index = -1
    pivot = nums[pivot_index]

    # will contain values less/more/equal to pivot
    left = []
    right = []
    middle = []

    # loop array and insert values accordingly
    for num in nums:
        if num > pivot:
            right.append(num)
        elif num < pivot:
            left.append(num)
        else:
            middle.append(num)

    # e.g. if k=2 and right=2/4. This means k largest value must be in thr right array
    if k <= len(right):
        return findKthLargest(right, k)
    # e.g. means k largest must be in left
    elif k > len(right) + len(middle):
        # we update the k to adjust for discarded values
        return findKthLargest(left, k - len(right) - len(middle))
    # else k largest is in the middle
    else:
        return pivot


nums = [3,2,1,5,6,4]

k=findKthLargest(nums,2)
print(k)
