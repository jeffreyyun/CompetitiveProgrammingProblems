# Flexible Spaces
# https://open.kattis.com/problems/flexible

W, P = [int(x) for x in input().split()]
locs = [int(x) for x in input().split()]
locs.append(W)
P += 1

g = {W}
for i in range(P):
    g.add(locs[i])
    for j in range(P):
        g.add(abs(locs[i]-locs[j]))

g = [i for i in g]
g.sort()
g = [str(i) for i in g[1:]]
print(' '.join(g))