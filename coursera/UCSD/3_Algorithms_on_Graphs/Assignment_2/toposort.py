#Uses python3

import sys

# Time: ~ V
# Space: ~ 2V


def dfs(adj, used, order, x):
    used[x] = 1
    for n in adj[x]:
        if not used[n]:
            dfs(adj, used, order, n)
    order.append(x)


def toposort(adj):
    used = [0] * len(adj)
    order = []
    # do DFS
    for v in range(len(adj)):
        if not used[v]:
            dfs(adj, used, order, v)
    # returns iterator, in reverse post-order
    return reversed(order)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')
    print();