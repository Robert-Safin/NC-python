# Given an array of integers nums and an integer k, return the total number
# of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

from typing import List

def subarraySum(nums: List[int], k: int) -> int:

    result = 0
    prefix_sum = 0
    # base case
    d = {0 : 1}

    for num in nums:
        prefix_sum += num

        # we check if we have any prefix (to the left of the current iteration)
        # that was can chop off and make the prefix sum == k
        if prefix_sum - k in d:
            # there can be multiple prefixes that match the scenario
            result = result + d[prefix_sum - k]

        # update hashmap
        if prefix_sum not in d:
            d[prefix_sum] = 1
        else:
            d[prefix_sum] = d[prefix_sum] + 1

    return result



nums = [2]
k = 2
subarraySum(nums,k) #2


# nums = [1,2,3]
# k = 3
# subarraySum(nums,k) #2


# nums = [-1,-1,1]
# k = 0
# subarraySum(nums,k) # 1
