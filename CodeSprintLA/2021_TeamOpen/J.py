import bisect
N, X, T = map(int, input().split()) # this is just BFS!!! get from 1 to X

h = [0]+list(map(int, input().split()))
d = [0]+list(map(int, input().split()))

# Reduce the number of things to search + sort (backwards!!)
startH = h[1]
endH = h[X]
actual = [(-h[i],d[i],i) for i in range(N+1)]
actual.sort()
l = bisect.bisect_left(actual, (-startH,))
r = bisect.bisect_left(actual, (-endH+1,))
actual = [(-1,-1,-1)] + actual[l:r]
N = len(actual)

# Get new start
for zz, (h,d,i) in enumerate(actual):
    if i == 1: start = zz
    if i == X: X = zz
# print(actual)
# print(N, X, T)

# can go i -> j if h[i] - h[j] <= d[j]
def solve(start=1):
    if X == start: return 0
    visited = [False for i in range(N+1)]

    curr = [start]
    visited[start] = True
    n = 0

    while len(curr) > 0:
        nxt = []
        for i in curr:
            # print(f"Visiting {i} {n}")
            l = bisect.bisect_left(actual, (actual[i][0],))
            for j in range(l,N+1):
                if not visited[j] and 0 <= (-actual[i][0] + actual[j][0]) <= actual[j][1]:
                    if j == X: return (n+1)*T
                    nxt.append(j)   # index in 'actual'
                    visited[j] = True
            curr = nxt
        n += 1
    return -1

ans = solve()
print(ans)
