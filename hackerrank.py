# # graph_snakes_and_ladders

import queue

def replace(adj, st, en, leng=100):
    for i in range(leng):
        for j in range(len(adj[i])):
            if adj[i][j] == st:
                adj[i][j] = en

T = int(input())
for t in range(T):
    visited = [False]*101
    adj = [[(i+j) for j in range(1,7) if i+j <= 100] for i in range(101)]
    n_l = int(input())
    loc = [i for i in range(100)]
    for l in range(n_l):
        st, en = [int(i) for i in input().split()]
        replace(adj, st, en)
    n_s = int(input())
    for s in range(n_s):
        st, en = [int(i) for i in input().split()]
        replace(adj, st, en)

    dist = [-1]*101
    q = queue.Queue()
    q.put(1)
    visited[1] = True
    dist[1] = 0
    while not q.empty():
        v = q.get()
        for n in adj[v]:
            if not visited[n]:
                visited[n] = True
                dist[n] = dist[v]+1
                q.put(n)
                if n == 100:
                    break
        
    print(dist[100])
        
    