import functools

@functools.lru_cache(None)
def solve(g, e):
    if e == 0 and g <= 2: return 1

    num = 0
    if e > 0:   # Kill Elder
        num += solve(g+1, e-1)
    if g >= 2:  # Kill Guardian
        num += solve(g-1, e)
    return num

T = int(input())

for t in range(T):
    G, E = map(int, input().split())
    ans = solve(G, E)
    print(ans)