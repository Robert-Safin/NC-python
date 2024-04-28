# Given an integer array nums of length n, you want to create an array ans
# of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).
from typing import List
def getConcatenation(nums: List[int]) -> List[int]:
    ans = []
    for _ in range(2):
        for i in nums:
            ans.append(i)

    return ans


print(getConcatenation([1,4,8]))
