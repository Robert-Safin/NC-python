
# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

# For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
# Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.

# You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

# Return a boolean array answer, where answer[j] is the answer to the jth query.

from typing import List,Dict,Tuple,Set

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj:Dict[int,List[int]] = {}

        for i in range(numCourses):
            adj[i] = []

        for pre,crs in prerequisites:
            adj[crs].append(pre)

        ans = []
        for pre,crs in queries:
            visited:Set[int] = set()
            ans.append(self.dfs(adj, pre, crs, visited))
        print(ans)
        return ans

    def dfs(self, adj:Dict[int,List[int]], query_pre:int, query_crs:int, visited:Set[int]):

        if query_crs in visited:
            return False

        visited.add(query_crs)

        if query_pre == query_crs:
            return True

        for pre in adj[query_crs]:
            if self.dfs(adj, query_pre, pre, visited):
                return True

        return False


sol = Solution()
numCourses = 5
prerequisites = [[0,1],[1,2],[2,3],[3,4]]
queries = [[0,4],[4,0],[1,3],[3,0]]
sol.checkIfPrerequisite(numCourses,prerequisites,queries) #[true,false,true,false]

numCourses = 2
prerequisites = [[1,0]]
queries = [[0,1],[1,0]]
sol.checkIfPrerequisite(numCourses,prerequisites,queries) #[false,true]
