# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites
# where prerequisites[i] = [ai, bi] indicates that you must take course bi first
# if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have
# to first take course 1.
# Return true if you can finish all courses. Otherwise, return false.
from typing import List,Dict,Set


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        preMap:Dict[int,List[int]] = {i: [] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visiting:Set[int] = set()

        for c in range(numCourses):
            if not self.dfs(c,visiting,preMap):
                return False
        return True


    def dfs(self, crs, visiting:Set[int], preMap:Dict[int,List[int]]):

                if crs in visiting:
                    return False

                if preMap[crs] == []:
                    return True

                visiting.add(crs)

                for pre in preMap[crs]:
                    if not self.dfs(pre,visiting,preMap):
                        return False

                visiting.remove(crs)
                preMap[crs] = []
                return True


sol = Solution()
p = [[1,0]]
print(sol.canFinish(2,p))
