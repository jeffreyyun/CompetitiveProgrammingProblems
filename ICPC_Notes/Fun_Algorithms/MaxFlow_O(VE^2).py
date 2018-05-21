"""
https://practice.geeksforgeeks.org/problems/find-the-maximum-flow/0

Given a graph with N vertices numbered 1 to N and M edges, the task is to find the max flow from vertex 1 to vertex N.

Input:
The first line of input contains an integer T denoting the no of test cases. Then T test cases follow. The first line of each test case contains two space separated integers N and M . Then in the next line are M space separated triplets x, y, z denoting an undirected edge from x to y with a flow capacity of z.

Output:
For each test case in a new line print a single integer denoting the maximum flow between 1 to N.


EDMOND-KARP ALGORITHM (implementation of Ford-Fulkerson)
Time: O(VE^2)
"""
from collections import defaultdict
import queue

class Solution:

    def findShortestPath(self):
        # uses BFS to find shortest path from vertices 1 to N in residual graph
        # stores path in self.parent
        parent = self.parent
        parent = [-1]*(N+1)     # stores BFS path

        graph = self.graph

        q = queue.Queue()
        q.put(1)

        while not q.empty():
            v = q.get()
            for neighbor in graph[v]:
                if parent[neighbor] == -1 and graph[v][neighbor] > 0:
                    q.put(neighbor)
                    parent[neighbor] = v

        self.parent = parent

        return parent[N] != -1



    def augment(self):
        # augments (updates) graph and max_flow
        graph = self.graph
        parent = self.parent

        # finds how much augmenting w/ the path produces additional flow
        path_flow = float('inf')
        source = 1
        curr = N
        while curr != source:
            path_flow = min(path_flow, graph[parent[curr]][curr])
            curr = parent[curr]

        # print("Path flow is ", path_flow)
        self.max_flow += path_flow

        # updates the graph
        curr = N
        while curr != source:
            graph[parent[curr]][curr] -= path_flow
            graph[curr][parent[curr]] += path_flow
            curr = parent[curr]

        return


    def EdmondKarp(self, graph, N, M):
        """
        while augmenting path exists with f
            pick shortest-hops path (via BFS)
            augment f by capacity(p)
        """
        self.N = N
        self.M = M
        self.max_flow = 0
        self.graph = graph
        self.parent = [-1]*(N+1)    # stores BFS path

        while self.findShortestPath():
            self.augment()

        return self.max_flow


T = int(input())
for t in range(T):
    # Read inputs
    N, M = map(int, input().split())
    triplets = [int(x) for x in input().split()]
    graph = defaultdict(dict)
    # Construct graph from inputs
    for _ in range(M):
        x, y, z = triplets[3*_ : 3*_+3]
        graph[x].setdefault(y, 0)
        graph[y].setdefault(x, 0)
        graph[x][y] += z
        graph[y][x] += z

    sol = Solution()
    max_flow = sol.EdmondKarp(graph, N, M)

    print(max_flow)
