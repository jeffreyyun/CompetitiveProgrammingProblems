#Problem        : Bathroom Crisis
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

def printGrid(grid):
    for r in grid:
        print(r)

def Dijkstra(mat, start, N):

    INF = 999

    visited = [None for i in range(N)]
    dists = [INF for i in range(N)]

    dists[start] = 0
    visited_count = 0

    while visited_count < N:
        v = dists.index(max(dists))
        for i in range(N):
            if not visited[i] and dists[i] <= dists[v]:
                v = i
        # v is now min with shortest-path guarantee that hasn't broadcast it yet
        visited[v] = True
        visited_count += 1
        for n in range(N):
            cost = adj[v][n]
            if dists[n] > dists[v] + cost:
                dists[n] = dists[v] + cost

    return dists


data = sys.stdin.read().splitlines()

UPSTAIRS = 20
DOWNSTAIRS = 10
ELEVWAIT = 15
ELEVMOVE = 5

N = int(data[0])
Blocs = [int(i) for i in data[1][1:].split()]
Elocs = [int(i) for i in data[2][1:].split()]
start = int(data[3])

# Dijkstra's shortest path to bathroom
adj = [[999 for i in range(N)] for j in range(N)]

# upstairs
for i in range(N):
    adj[i][i] = 0
    for j in range(i+1, N):
        adj[i][j] = UPSTAIRS*(j - i)
for i in range(N):
    for j in range(i):
        adj[i][j] = DOWNSTAIRS*(i - j)
# elevators
for i in Elocs:
    for j in Elocs:
        adj[i][j] = min(adj[i][j], ELEVWAIT + ELEVMOVE*abs(i-j))
    
best_dist = 999

dists = Dijkstra(adj, start, N)
for i in Blocs:
    best_dist = min(best_dist, dists[i])

print(best_dist)