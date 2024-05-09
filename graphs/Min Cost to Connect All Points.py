# You are given an array points representing integer coordinates of some points
# on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance
# between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if
# there is exactly one simple path between any two points.

from typing import List,Tuple,Dict,Set
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adj:Dict[Tuple[int,int],List[Tuple[int,int,int]]] = {}

        # gen adj list where each point is connected to all other points
        for x,y in points:
            adj[(x,y)] = []

            for x2,y2 in points:
                if (x,y) != (x2,y2):
                    dst = self.manhat(x,x2,y,y2)
                    adj[(x,y)].append((dst,x2,y2))


        min_heap:List[Tuple[int,int,int]] = [(0,points[0][0],points[0][1])]
        visited:Set[Tuple[int,int]] = set()
        min_distance = 0

        while min_heap:
            popped_distance, popped_x, popped_y = heapq.heappop(min_heap)

            # dont revisit
            if (popped_x,popped_y) in visited:
                continue

            # update distance
            min_distance += popped_distance
            visited.add((popped_x,popped_y))

            # add neighbors
            for neighbor_weight, neighbor_x, neighbor_y in adj[(popped_x,popped_y)]:
                if (neighbor_x,neighbor_y) not in visited:
                    heapq.heappush(min_heap,(neighbor_weight,neighbor_x,neighbor_y))

        return min_distance

    def manhat(self,x1:int ,x2:int ,y1:int ,y2:int) -> int:
        return abs(x1-x2) + abs(y1-y2)

sol = Solution()
points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
sol.minCostConnectPoints(points) # Output: 20
