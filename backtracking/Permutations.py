# Given an array nums of distinct integers, return all the possible permutations.
# You can return the answer in any order.




from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    perms:List[List[int]] = [[]]

    for n in nums:
        nextPerms = []

        for p in perms:

            for i in range(len(p) + 1):
                pCopy = p.copy()
                pCopy.insert(i, n)
                nextPerms.append(pCopy)

        perms = nextPerms
    print(perms)
    return perms







nums = [1,1,2]
permute(nums) #[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
