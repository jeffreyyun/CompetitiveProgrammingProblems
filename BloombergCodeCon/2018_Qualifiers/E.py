#Problem        : Fastest Flight
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import queue

N = int(input())
adj = {}
visited = {}
for _ in range(N):
    line = input().split()
    O, D, dur, _ = line[:4]
    dep = list(map(int, line[4:]))
    adj.setdefault(O, {})
    adj.setdefault(D, {})
    adj[O].setdefault(D, {})
    adj[O][D]["dur"] = int(dur)
    adj[O][D]["dep"] = dep
    visited[O] = False
    visited[D] = False
for O in adj:
    for D in adj[O]:
        adj[O][D]["dep"].sort()

# find start and dest
OO, DD, start = input().split()
start = int(start)

# check if possible
q = queue.Queue()
q.put(OO)
while not q.empty():
    curr = q.get()
    visited[curr] = True
    if curr == DD:
        break
    for d in adj[curr]:
        if not visited[d]:
            visited[d] = True
            q.put(d)

def solve():
    # use priority queue w/ current time
    pq = queue.PriorityQueue()
    pq.put((start, OO))
    while not pq.empty():
        curr, currO = pq.get()
        # print(curr, currO)
        if currO == DD:
            return curr - start

        # Take the next possible flight, period!
        curr_t = curr % 1440
        for dest in adj[currO]:
            no_flight = True
            for t in adj[currO][dest]["dep"]:
                if not no_flight:
                    continue
                if t >= curr_t:
                    # take this flight!
                    nt = curr + (t-curr_t) + adj[currO][dest]["dur"]
                    pq.put((nt, dest))
                    no_flight = False
            # Try taking the earliest flight the next day
            if no_flight:
                t = adj[currO][dest]["dep"][0]
                nt = curr + (1440+t-curr_t) + adj[currO][dest]["dur"]
                pq.put((nt, dest))
    raise Exception()


if DD not in visited or not visited[DD]:
    print("IMPOSSIBLE")
else:
    print(solve())
