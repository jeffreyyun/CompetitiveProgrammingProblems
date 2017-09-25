#!/bin/python3

# Union-Find algorithm does not work after 60 minutes debugging

class DisjointSet(object):      # weighted union-find with path compression

    def __init__(self, n):
        self.size = [1 for i in range(n)]
        self.parent = [i for i in range(n)]

    def find(self, p):
        # find the root
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]

        # root = p
        # while root != self.parent[root]:
        #     root = self.parent[root]
        # while p != self.parent[p]:
        #     newp = self.parent[p]
        #     self.parent[p] = root;
        #     p = newp;

        return p

    def union(self, p, q):
        r1 = self.find(p)
        r2 = self.find(q)
        if r1 == r2:
            return
        if self.size[p] >= self.size[q]:
            r1, r2 = p, q
        else:
            r1, r2 = q, p
        self.parent[r2] = r1
        self.size[r1] += self.size[r2]
        self.size[r2] = self.size[r1]


class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # db1 = 17
        # db2 = 5

        DS = DisjointSet(2001) # n_v = n_e here
        redundant = None
        for p, q in edges:
            # if (p == db1 and q == db2):
            #     print(DS.parent[db1], "|", DS.parent[db2])
            if DS.find(p) != DS.find(q):
                DS.union(p, q)
            else:
                redundant = [p,q]

        return redundant


sol = Solution()
inp = [[15,5],[2,8],[5,6],[10,12],[7,16],[10,3],[12,17],[10,8],[14,13],[10,6],[17,5],[20,19],[16,4],[20,18],[19,14],[1,4],[16,20],[16,6],[11,10],[12,9]]
r = sol.findRedundantConnection(inp)

print(r)

