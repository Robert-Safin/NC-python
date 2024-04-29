# Given a circular integer array nums of length n, return the maximum
# possible sum of a non-empty subarray of nums.

# A circular array means the end of the array connects to the beginning
# of the array. Formally, the next element of nums[i] is nums[(i + 1) % n]
# and the previous element of nums[i] is nums[(i - 1 + n) % n].

# A subarray may only include each element of the fixed buffer nums at most
# once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j],
# there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

from typing import List


def maxSubarraySumCircular(nums: List[int]) -> int:

    # count total sum of array
    array_sum = 0

    # Kadane's max sum slice
    max_sum = nums[0]
    max_curr_sum = 0

    # Kadane's min sum slice
    min_sum = nums[0]
    min_curr_sum = 0

    # run Kadane's
    for n in nums:

        # array sum
        array_sum += n

        # Kadane's max sum slice
        max_curr_sum += n
        max_curr_sum = max(max_curr_sum, 0)
        max_sum = max(max_curr_sum, max_sum)

        # Kadane's min sum slice
        min_curr_sum += n
        min_curr_sum = min(min_curr_sum, 0)
        min_sum = min(min_curr_sum, min_sum)

    # edge case for all negative vals in array
    # e.g   sum == -10, min_sum == -10
    #       -10 - -10 == 0
    # hence we want to return the max_sum, which will be single greatest value in array
    if array_sum == min_sum:
        return max_sum
    # max_sum is greatest slice for normal array
    # array_sum - min_sum is greatest slice for circular array
    else:
        return max(max_sum, array_sum - min_sum)


nums = [-3,-2,-3]

print(maxSubarraySumCircular(nums))
