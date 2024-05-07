# You are given a network of n nodes, labeled from 1 to n. You are also given
# times, a list of travel times as directed edges times[i] = (ui, vi, wi),
# where ui is the source node, vi is the target node, and wi is the time it
# takes for a signal to travel from source to target.

# We will send a signal from a given node k. Return the minimum time it takes
# for all the n nodes to receive the signal. If it is impossible for all the n
# nodes to receive the signal, return -1.



from typing import List,Dict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        adjacency_list:Dict[int,List[List[int]]] = {}

        for source, destination, weight in times:
            if source not in adjacency_list:
                adjacency_list[source] = []
            if destination not in adjacency_list:
                adjacency_list[destination] = []
            adjacency_list[source].append([destination, weight])

        shortest_paths:Dict[int,int] = {}

        min_heap = [ [0, k] ]

        while min_heap:
            popped_weight, popped_node = heapq.heappop(min_heap)

            if popped_node in shortest_paths:
                continue

            shortest_paths[popped_node] = popped_weight

            for neighbor, neighbor_weight in adjacency_list[popped_node]:
                if neighbor not in shortest_paths:
                    heapq.heappush(min_heap,[popped_weight+neighbor_weight, neighbor])


        if len(shortest_paths) != n:
            return -1

        return max(shortest_paths.values())



sol = Solution()
            #from,to,time
times = [   [2,1,1],
            [2,3,1],
            [3,4,1] ]
# number of nodes
n = 4
# source node
k = 2

print(sol.networkDelayTime(times,n,k)) # 2
