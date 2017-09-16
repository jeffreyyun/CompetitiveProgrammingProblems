#Uses python3

import sys

sys.setrecursionlimit(200000)

# Time: ~ V + 3E 
# Space: ~ 3V + E

def explore(adj, visited, x):
    visited[x] = 1
    for n in adj[x]:
        if not visited[n]:
            explore(adj, visited, n);

def dfs(adj, visited, order, x):
    # runs DFS and places vertexes in post-order
    visited[x] = 1
    for n in adj[x]:
        if not visited[n]:
            dfs(adj, visited, order, n)
    order.append(x)

def number_of_strongly_connected_components(adj):
    result = 0

    # reverse the graph (V+E)
    reversed_adj = [[] for i in range(len(adj))]
    for v in range(len(adj)):
        for n in adj[v]:
            reversed_adj[n].append(v)

    # run DFS on G^R (E)
    # --> larger post-order attached to vertexes in sink SCC's in adj
    visited =[0]*len(adj)
    order = []
    for v in range(len(adj)):
        if not visited[v]:
            dfs(reversed_adj, visited, order, v);

    # traverse v (E)
    visited =[0]*len(adj)
    # go in reversed post-order
    for v in reversed(order):
        # if not visited, explore and mark as visited
        if not visited[v]:
            # since sink, all reachable components are interconnected
            explore(adj, visited, v)
            # new sink SCC
            result += 1              
    return result

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(number_of_strongly_connected_components(adj))
