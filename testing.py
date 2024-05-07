import heapq
from typing import List, Dict

# Given a connected graph represented by a list of edges, where
# edge[0] = src, edge[1] = dst, and edge[2] = weight,
# find the shortest path from src to every other node in the
# graph. There are n nodes in the graph.
# O(E * logV), O(E * logE) is also correct.
def shortestPath(edges, src):
    # create adjacency list which maps node to its neighbors with vertices and weight to that neighbor
    adjacency_list: Dict[int, List[List[int]]] = {}

    # create key entries with empty values
    for source, destination, weight in edges:
        # some nodes might not have vertices from them,
        # so need to create empty entries for both dest and source
        if source not in adjacency_list:
            adjacency_list[source] = []
        if destination not in adjacency_list:
            adjacency_list[destination] = []
        # finally build adjacency list
        adjacency_list[source].append([destination, weight])

    # map where Node : shortest distance from start
    shortest_paths: Dict[int, int] = {}

    # min heap is used to pop the smallest weight neighbor available.
    # first value will be used for ordinal comparison (at least in python)
    # init heap with the origin node and 0 distance
    min_heap = [[0, src]]


    while min_heap:
        # pop smallest distance from min heap
        popped_weight, popped_node = heapq.heappop(min_heap)

        # the way the algo works, the first time a node is visited, this is the shortest path to it
        # so if a node is revisited it will only generate longer path
        # skip this loop iteration
        if popped_node in shortest_paths:
            continue

        # shortest path is now found for popped node
        shortest_paths[popped_node] = popped_weight

        # now we need to get all the neighbors of the popped node and add them to heap
        for neighbor, neighbor_weight in adjacency_list[popped_node]:
            # avoid infinite loops where A->B and B->A
            if neighbor not in shortest_paths:
                # add the neighbor to the heap with the weight of the path to it
                # where the weight of the path to the neighbor is the weight of the path
                # to the popped node plus the weight of the edge to the neighbor
                heapq.heappush(min_heap, [popped_weight + neighbor_weight, neighbor])

    return shortest_paths

edges = [['A', 'B',10],
         [ 'A', 'C', 3],
         [ 'C', 'B', 4],
         [ 'C', 'D', 8],
         [ 'C', 'E', 2],
         [ 'B', 'D', 2],
         [ 'D', 'E', 5] ]

shortestPath(edges, 'A')
