# Given an integer array nums of unique elements, return all possible
# subsets
#  (the power set).

# The solution set must not contain duplicate subsets. Return the solution
# in any order.

from typing import List

def dfs(nums: List[int], i: int, subset: List[int], res: List[List[int]]):

    if i >= len(nums):
        res.append(subset.copy())
        return

    # Include nums[i] in the subset
    subset.append(nums[i])
    dfs(nums, i + 1, subset, res)

    # Do not include nums[i] in the subset
    subset.pop()
    dfs(nums, i + 1, subset, res)




def subsets(nums: List[int]) -> List[List[int]]:
    res:List[List[int]] = []
    subset:List[int] = []


    dfs(nums, 0, subset, res)
    return res


nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

subsets(nums)
