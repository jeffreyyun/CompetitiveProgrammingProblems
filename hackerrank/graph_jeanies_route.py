# from copy import deepcopy

# def cutTree(adj, targets):
#     # forms a Steiner tree of the target nodes
#     # remove edges not contributing to path to targets (Steiner tree) until all are gone
#     while True:
#         extraFound = False
#         for v in list(adj.keys()):
#             if not targets[v] and len(adj[v]) == 1:
#                 extraFound = True
#                 u,d = adj[v][0]
#                 adj[v].remove((u,d))
#                 adj[u].remove((v,d))
#                 del(adj[v])
#         if not extraFound:
#             break
#     return


# def totalLength(adj):
#     # Gets Eulerian path of the acyclic Steiner tree
#     cost = 0
#     for v in adj.keys():
#         for e in adj[v]:
#             cost += e[1]  # adds distance component of tuple
#     return cost

# def tryDFS(adj, curr, prev_cost, max_cost, visited):
#     # marks as visited
#     visited[curr] = True
#     # try all connected nodes
#     for n in adj[curr]:
#         curr_cost = 0
#         # go into node if not visited
#         if not visited[n[0]]:
#             curr_cost = prev_cost + n[1]
#             max_cost[0] = max(max_cost[0], curr_cost)
#             max_cost[0] = max(max_cost[0], tryDFS(adj, n[0], curr_cost, max_cost, visited))
#     return max_cost[0]


# def largestCostPath(adj, n):
#     costs = 0
#     # finds longest path from one vertex to any other
#     for v in adj.keys():
#         max_cost = [0]
#         visited = [False for i in range(n+1)]
#         tryDFS(adj, v, 0, max_cost, visited)
#         costs = max(costs, max_cost[0])
#     return costs


# if '__main__' == __name__:
#     n, k = [int(i) for i in input().split()]
#     targets = [False for i in range(n+1)]
#     for i in input().split():
#         targets[int(i)] = True

#     # forms adjacency list, dictionary for node deletion
#     adj = {}
#     for i in range(1, n+1):
#         adj[i] = []
#     for i in range(n-1):
#         u,v,d = [int(i) for i in input().split()]
#         adj[u].append((v,d))
#         adj[v].append((u,d))

#     cutTree(adj, targets)
#     result = totalLength(adj)
#     result -= largestCostPath(adj, n)
#     print(result)


import sys
sys.setrecursionlimit(100000)

# Graph is undirected, acyclic
M = 0               # the longest total path between two targets
edgeSum = 0         # the sum of all edges that must be traversed
targets = []
necessity = []
adj = {}

def go(curr, prev):
    global M, edgeSum, adj, targets, necessity
    # The second longest and longest paths downstream from this vertex
    # in the beginning, there are no paths, so their lengths are -inf
    second_longest = -float('inf')
    longest = -float('inf')

    for neighbor, cost in adj[curr]:
        if neighbor != prev:    # don't go back the same way

            # find the distance covering all the targets when we go in this branch
            longest_from_neighbor = go(neighbor, curr)
            second_longest = max(second_longest, longest_from_neighbor + cost)

            # swaps when appropriate
            if second_longest > longest:
                second_longest, longest = longest, second_longest

            # necessity accounts for the intermediate cities, which are necessary to reach the targets
            necessity[curr] += necessity[neighbor]    # necessary to get to neighbor

            # this edge is necessary
            # second term cuts off starting edges if all targets are downstream
            if necessity[neighbor] != 0 and necessity[neighbor] != k:
                edgeSum += cost

    # two branches lead to targets
    if second_longest > 0:
        M = max(M, longest+second_longest)

    # distance from vertex to farthest target downstream
    if longest > 0 and targets[curr]:
        M = max(M, longest)

    # when it is returned, `second_longest` will get the value `cost`
    if targets[curr]:
        longest = max(longest, 0)

    return longest


if '__main__' == __name__:
    # Get inputs
    n, k = [int(i) for i in input().split()]
    # targets --> cities Jeanie must go to
    targets = [False for i in range(n+1)]
    necessity = [0 for i in range(n+1)]
    for i in input().split():
        targets[int(i)] = True
        necessity[int(i)] = 1

    # Forms adjacency list, as a dictionary with tuples entries (neighbor, cost)
    for i in range(1, n+1):
        adj[i] = []
    for i in range(n-1):
        u,v,d = [int(i) for i in input().split()]
        adj[u].append((v,d))
        adj[v].append((u,d))

    go(1,1)
    print(edgeSum*2 - M)

