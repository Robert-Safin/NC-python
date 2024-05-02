# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:

    # empty array with 1 (handle multiplication by 0)
    # one extra element is also added to handle going out of bounds
    # the idea is to take the prefix product before index and multiply it by
    # postfix product after the index
    result = [1 for _ in range(len(nums) +1 )]

    # calculate prefix product and insert into result[i+1]
    prefix = 1
    for i in range(len(nums)):
        prefix *= nums[i]
        result[i+1] = prefix

    # calculate postfix product and multiply it by prefix at
    postfix = 1
    for i in reversed(range(len(nums))):
        postfix *= nums[i]
        result[i-1] *= postfix

    # remove the extra padding element
    return result[:-1]

productExceptSelf([1,2,3,4])
                            #pre  [1, 2, 6, 24]
                            #post [24,24,12,4]
                            # [24,12,8,6]


#productExceptSelf([-1,1,0,-3,3]) #[0,0,9,0,0]
# [1,3,4]

#print()
