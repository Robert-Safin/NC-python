
# Given a reference of a node in a connected undirected graph.

# Return a deep copy (clone) of the graph.



from typing import Optional,List,Deque,Dict
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors:List['Node'] = []):
        self.val = val
        self.neighbors = neighbors



class Solution:
    def cloneGraph(self, node: Node) -> Node:

        oldToNew:Dict[int,int] = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            copy = Node(node.val)
            oldToNew[node] = copy
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
            return copy

        return dfs(node) if node else None
