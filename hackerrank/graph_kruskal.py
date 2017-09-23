# Implementation of Kruskal's Algorithm

import queue

class DS():
    def __init__(self, n):
        self.size = [1]*n
        self.root = [i for i in range(n)]
        
    def find(self, n):
        while n != self.root[n]:
            self.root[n] = self.root[self.root[n]]
            n = self.root[n]
        return n
    
    def union(self, p, q):
        p,q = self.root[p], self.root[q]
        if self.size[p] > self.size[q]:
            r1, r2 = p, q
        else:
            r1, r2 = q, p
        self.root[r2] = r1
        self.size[r1] += self.size[r2]
        self.size[r2] = self.size[r1]
        
n_v, n_e = [int(i) for i in input().split()]
edges = queue.PriorityQueue()
ds = DS(n_v)
for i in range(n_e):
    a, b, c = [int(i) for i in input().split()]
    edges.put((c, (a,b)))
result = 0

for i in range(n_v-1):
    if edges.empty():
        print('error')
        break
    c,d = edges.get()
    a,b = d
    while not edges.empty() and ds.find(a-1) == ds.find(b-1):
        c,d = edges.get()
        a,b = d
    ds.union(a-1,b-1)
    result += c
print(result)
