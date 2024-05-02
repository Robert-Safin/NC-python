# Given an array of integers nums and an integer k, return the total number
# of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

from typing import List,Dict

def subarraySum(nums: List[int], k: int) -> int:
    count = 0
    sum = 0
    # handle cases where the subarray starts from the beginning of the array
    dic:Dict[int,int] = {0:1}

    for i in range(len(nums)):
        sum += nums[i]

        # check if there exists a prefix sum that differs
        # from the current prefix sum by exactly k
        if sum-k in dic:
            count += dic[sum-k]

        # update
        dic[sum] = dic.get(sum, 0) + 1

    print(count)
    return count


nums = [1,1,1]
k = 2
subarraySum(nums,k) #2


nums = [1,2,3]
k = 3
subarraySum(nums,k) #2


nums = [-1,-1,1]
k = 0
subarraySum(nums,k) # 1
