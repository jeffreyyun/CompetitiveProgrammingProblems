# For some reason, gets wrong answer...

def solve():
    R, B, C = map(int, input().split())
    cashiers = []
    for _ in range(C):
        M, S, P = map(int, input().split())
        cashiers.append((M, S, P))

    # Perform binary search on T -- what is the minimum time for a subset of <= R cashiers to service B bits?
    lo = 0
    hi = max(cashiers, key = lambda x: x[0]*x[1]+x[2])
    hi = hi[0]*hi[1]+hi[2]
    capacity = [0 for _ in range(C)]
    while lo <= hi:
        T = lo + (hi - lo)//2
        for i in range(C):
            M, S, P = cashiers[i]
            capacity[i] = min(M, (T - P)/S//1)
        capacity.sort()
        if sum(capacity[C-min(C,R):]) >= B: # if we meet the demand
            hi = T - 1
        else:
            lo = T + 1
    return lo

T = int(input())
for t in range(T):
    ans = solve()
    print("Case #{}: {}".format(t+1, ans))
