# In this problem, a tree is an undirected graph that is connected and has no cycles.

# You are given a graph that started as a tree with n nodes labeled from 1 to n,
# with one additional edge added. The added edge has two different vertices chosen
# from 1 to n, and was not an edge that already existed. The graph is represented
# as an array edges of length n where edges[i] = [ai, bi] indicates that there is
# an edge between nodes ai and bi in the graph.

# Return an edge that can be removed so that the resulting graph is a tree of
# n nodes. If there are multiple answers, return the answer that occurs last in the input.
from typing import List,Dict

class UnionFind:
    def __init__(self, n):
        # maps node(k) to its parent(v)
        self.par = {}
        # maps node(k) to its rank(v)
        self.rank = {}

        # in this problem nodes value are 1..len(edge)
        # assign nodes parent to self and rank to 0
        for i in range(1, n + 1):
            self.par[i] = i
            self.rank[i] = 0

    # find node's parent
    def find(self, n):
        # set 'current' pointer
        p = self.par[n]

        # inited nodes with self as parents, so if we find node who is its own parent, its the head
        while p != self.par[p]:
            # optimization to cut stack frames in half
            # same as self.par[p] = self.par[p]
            self.par[p] = self.par[self.par[p]]
            # update 'current' pointer
            p = self.par[p]
        # return the parent
        return p

    def union(self, n1, n2):

        # get parents of both nodes
        p1, p2 = self.find(n1), self.find(n2)

        # same parents means connecting these nodes will result in loop
        if p1 == p2:
            return False

        # optimization, attach smaller tree to larger tree
        # same as leaving only: self.par[p2] = p1 instead of the entire if statement
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1

        # indicate union was successful
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        union_find = UnionFind(len(edges))

        for edge in edges:
            if not union_find.union(edge[0], edge[1]):
                return edge
        return []
