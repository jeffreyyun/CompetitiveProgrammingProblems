#Uses python3

import sys

# Time: O(V + E), ~(2V + E)
# Space: ~ 3V


def find_postorder(adj, visited, order, x):
    visited[x] = 1
    for n in adj[x]:
        if not visited[n]:
            find_postorder(adj, visited, order, n)
    order.append(x)

def acyclic(adj):

    visited = [0]*len(adj)
    order = []
    post_order = [0]*len(adj)
    # find post-order of every vertex
    for v in range(len(adj)):
        if not visited[v]:
            find_postorder(adj, visited, order, v)
    for i in range(len(adj)):
        post_order[order[i]] = i

    # check for each u-->v, post(u) > post(v)
    for v in range(len(adj)):
        for n in adj[v]:
            # if v-->n, yet post(v) < post(n)
            if post_order[v] < post_order[n]:
                return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
