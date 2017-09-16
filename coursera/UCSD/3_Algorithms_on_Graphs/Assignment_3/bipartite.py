#Uses python3

import sys
import queue

def bipartite(adj):
    # looking for bipartiteness of only the connected component containing first vertex

    dist = [-1]*len(adj)
    dist[0] = 0

    # straightforward bfs
    visited = [False]*len(adj)
    visited[0] = True
    q = queue.Queue()
    q.put(0)
    while not q.empty():
        v = q.get()
        for n in adj[v]:
            if not visited[n]:
                visited[n] = True
                q.put(n)
                dist[n] = dist[v] + 1

    # checks to see if vertex and a neighbor in same partition
    for v in range(len(adj)):
        for n in adj[v]:
            if visited[v] and (dist[v]%2) == (dist[n]%2):
                return 0

    return 1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
