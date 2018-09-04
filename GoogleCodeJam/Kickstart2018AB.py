def solve(N, K, V):
    import bisect
    # preprocessing -- reverse sort
    V.sort()
    if V[0] == V[-1]:
        return V[0] # all the same
    rollingSums = V[:] + [0]
    for i in range(N-1, -1, -1):
        rollingSums[i] += rollingSums[i+1]

    EV = [0 for i in range(K + 1)]
    EV[0] = rollingSums[0]/N
    for i in range(1, K + 1):
        ind = bisect.bisect(V, EV[i-1])
        numsLarger = N - ind
        sumLarger = rollingSums[ind]
        mult = (numsLarger / N)     # get the prize now
        # print("sumlarger: {}, mult: {}, numsLarger: {}".format(sumLarger, mult, numsLarger))
        if numsLarger != 0:
            EV[i] = sumLarger/numsLarger * mult + (1 - mult) * EV[i - 1]   # get the prize now, or try again
        else:
            EV[i] = (1 - mult) * EV[i - 1]   # get the prize now, or try again
    return EV[-1]


T = int(input())
for t in range(T):
    N, K = map(int, input().split())
    V = list(map(int, input().split()))
    print("Case #{}: {}".format(t+1, solve(N, K, V)))
