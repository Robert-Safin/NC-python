# You are given an undirected weighted graph of n nodes (0-indexed),
# represented by an edge list where edges[i] = [a, b] is an undirected
# edge connecting the nodes a and b with a probability of success of
# traversing that edge succProb[i].

# Given two nodes start and end, find the path with the maximum
# probability of success to go from start to end and return its
# success probability.

# If there is no path from start to end, return 0. Your answer
# will be accepted if it differs from the correct answer by at most 1e-5.

from typing import List,Dict,Tuple
import heapq

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj_list:Dict[int,List[Tuple[int,float]]] = {}

        new_edges = []

        # generate adj list for UNDIRECTED graph
        for i in range(len(edges)):
            src = edges[i][0]
            dst = edges[i][1]
            prob = succProb[i]
            tup = (src,dst,prob)
            tup2 = (dst,src,prob)
            new_edges.append(tup)
            new_edges.append(tup2)

        for i in range(n):
            adj_list[i] = []

        for src,dst,prob in new_edges:
            adj_list[src].append((dst,prob))

        shortest_paths:Dict[int,float] = {}

        # negated min heap -> max heap
        max_heap:List[Tuple[float,int]] = [(-1.0, start_node)]

        while max_heap:
            popped_prob, popped_node = heapq.heappop(max_heap)

            # avoid infinite loop between 2 nodes
            if popped_node in shortest_paths:
                continue

            # update shortest paths, negate
            shortest_paths[popped_node] = popped_prob *-1

            # early return of end node reached, negate
            if popped_node == end_node:
                return popped_prob *-1

            # add neighbors
            for neighbor, neighbor_prob in adj_list[popped_node]:
                if neighbor_prob not in shortest_paths:
                    # since the first value manually added to max_heap was negative,
                    # 'popped_prob * neighbor_prob' will always result in negated value
                    # as one is always negative and other positive
                     heapq.heappush(max_heap, (popped_prob * neighbor_prob, neighbor))


        # end node is unreachable
        return 0




sol = Solution()

n = 3
edges = [[0,1],[1,2],[0,2]]
succProb = [0.5,0.5,0.2]
start = 0
end = 2

print(sol.maxProbability(n, edges,succProb, start,end)) # 0.25000


n =5
edges =[[1,4],[2,4],[0,4],[0,3],[0,2],[2,3]]
succProb =[0.37,0.17,0.93,0.23,0.39,0.04]
start_node =3
end_node =4

print(sol.maxProbability(n, edges,succProb, start_node,end_node)) # 0.21390
