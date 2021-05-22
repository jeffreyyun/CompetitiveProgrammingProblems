parent = dict()
rank = dict()

def make_set(vertice):
    parent[vertice] = vertice
    rank[vertice] = 0

def find(vertice):
    if parent[vertice] != vertice:
        parent[vertice] = find(parent[vertice])
    return parent[vertice]

def union(vertice1, vertice2):
    root1 = find(vertice1)
    root2 = find(vertice2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]: rank[root2] += 1

def kruskal(graph):
    for vertice in graph['vertices']:
        make_set(vertice)
        minimum_spanning_tree = set()
        edges = list(graph['edges'])
        edges.sort()
    #print edges
    for edge in edges:
        weight, vertice1, vertice2 = edge
        if find(vertice1) != find(vertice2):
            union(vertice1, vertice2)
            minimum_spanning_tree.add(edge)

    return sorted(minimum_spanning_tree)

import collections
import heapq

def minCostConnectPoints(points):
    manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
    n, c = len(points), collections.defaultdict(list)
    for i in range(n):
        for j in range(i+1, n):
            d = manhattan(points[i], points[j])
            c[i].append((d, j))
            c[j].append((d, i))
    cnt, ans, visited, heap = 1, 0, [0] * n, c[0]
    visited[0] = 1
    heapq.heapify(heap)
    while heap:
        d, j = heapq.heappop(heap)
        if not visited[j]:
            visited[j], cnt, ans = 1, cnt+1, ans+d
            for record in c[j]: heapq.heappush(heap, record)
        if cnt >= n: break
    return ans

N = int(input())
points = []
for _ in range(N):
    points.append(list(map(int, input().split())))
ans = minCostConnectPoints(points)
print(ans*2)
