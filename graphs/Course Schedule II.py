# There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

# For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
# Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

from typing import List,Dict,Set




class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        adj:Dict[int,List[int]] = {}
        visit:Set[int] = set()
        order:List[int] = []
        path:Set[int] = set()

        # generate adj list
        for i in range(numCourses):
            adj[i] = []
        for crs, pre in prerequisites:
            adj[crs].append(pre)


        # need to call dfs on each node as there could be disconnected 'islands'
        # as well as since the graph is directed, and we dont know the 'head'
        # entering at a random node does not mean we see all nodes.

        for course in adj.keys():
            if self.dfs(course, path, visit, adj, order) == False:
                return[]

        return order

    def dfs(self, crs:int, path:Set[int], visit:Set[int], adj:Dict[int,List[int]], order:List[int]):
        # first base case, this detects a cycle
        if crs in path:
            return False

        # ignore visited, speeds up process in non cyclical graphs and prevent inf loop in cyclical
        if crs in visit:
            return True

        # update path
        path.add(crs)

        # dfs all neighbors of current node
        for pre in adj[crs]:
            if self.dfs(pre, path, visit, adj, order) == False:
                return False

        # once a 'dead end' node is reached this part can run.
        # pop path to allow earlier stack calls to re explore node via different path
        path.remove(crs)
        # update visit
        visit.add(crs)
        # append 'dead end' node
        order.append(crs)
        return True

sol = Solution()

# numCourses = 2
# prerequisites = [[1,0]]
# sol.findOrder(numCourses,prerequisites) # [0,1]


numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(sol.findOrder(numCourses,prerequisites))# [0,2,1,3]




# class Solution:
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

#         adj:Dict[int,List[int]] = {}
#         order:List[int] = []


#         # generate adjacency list
#         for i in range(numCourses):
#             adj[i] = []
#         for crs, pre in prerequisites:
#             adj[crs].append(pre)

#         # while there are still courses with no prerequisites
#         while any(not prerequisites for prerequisites in adj.values()):
#             # find courses with no prerequisites
#             for course in adj.keys():
#                 if adj[course] == []:
#                     # add course with no prerequisites to order
#                     order.append(course)
#                     # remove course with no prerequisites from prerequisites of other courses
#                     for pre in adj.keys():
#                         if course in adj[pre]:
#                             adj[pre].remove(course)
#                     # remove key entry
#                     adj.pop(course)
#                     # break loop to recheck for courses with no prerequisites
#                     break

#         # no keys remain, all course have been completed
#         if adj == {}:
#             return order
#         # if keys remain, there are still courses with prerequisites (impossible to complete)
#         else:
#             return []
