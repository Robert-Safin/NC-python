# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.
from typing import List,Dict

class Solution:

    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        parents = [i for i in range(len(nums))]
        ranks = [0 for i in range(len(nums))]
        number_index = {}

        for i, num in enumerate(nums):
            if num in number_index:
                continue
            number_index[num] = i
            if num-1 in number_index:
                self.union(parents, ranks, i, number_index[num-1])
            if num+1 in number_index:
                self.union(parents, ranks, i, number_index[num+1])

        count:Dict[int,int] = {}
        for i, num in enumerate(nums):
            p = self.find_parent(parents, i)
            if p in count:
                count[p] += 1
            else:
                count[p] = 1

        return max(count.values())

    def find_parent(self, parents:List[int], number_index:int):
        p = parents[number_index]
        if p == number_index:
            return p
        else:
            return self.find_parent(parents, p)

    def union(self, parents:List[int], ranks:List[int], number1:int, number2:int):
        p1 = self.find_parent(parents, number1)
        p2 = self.find_parent(parents, number2)
        if p1 == p2:
            return
        if ranks[p1] > ranks[p2]:
            parents[p2] = p1
        elif ranks[p1] < ranks[p2]:
            parents[p1] = p2
        else:
            parents[p1] = p2
            ranks[p2] += 1


nums = [100,4,200,1,3,2]
sol = Solution()
sol.longestConsecutive(nums) # 4
