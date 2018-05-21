def solve():
    def fmax(a, b):
        return a if len(a) >= len(b) else b

    N = int(input())
    W = list(map(int, input().split()))
    maxW = 6*sum(W)
    dp = [[0 for j in range(maxW+1)]]
    # for i in range(1, N+1):
    #     W[i-1] = W[i-1]
    #     for w in range(min(maxW-W[i-1]+1, W[i-1]*6+1)):
    #         dp[i][w+W[i-1]] = max(dp[i-1][w+W[i-1]], dp[i-1][w]+1)
    for i in range(1, N+1):
        dp.append([0 for _ in range(W[i-1])] + [max(dp[i-1][w+W[i-1]], dp[i-1][w]+1) for w in range(min(maxW-W[i-1]+1, W[i-1]*6+1))] + [0 for _ in range(maxW+1-min(maxW-W[i-1]+1, W[i-1]*6+1))])
    return max(dp[-1])
    # dp[1:] = [[max(dp[i-1][w], dp[i-1][w-W[i-1]]+1) if W[i-1] <= w < min(maxW-W[i-1]+1, W[i-1]*6+1) else dp[i][w] for w in range(maxW+1)] for i in range(1, N+1)]

    # dp = [[[] for j in range(maxW+1)] for i in range(N+1)]
    # for i in range(1, N+1):
    #     W[i-1] = W[i-1]
    #     for w in range(min(maxW - W[i-1], W[i-1]*6+1)):
    #         dp[i][w+W[i-1]] = fmax(dp[i][w+W[i-1]], dp[i-1][w]+[i-1])
    #         dp[i][w] = fmax(dp[i][w], dp[i-1][w])
    # for r in dp:
    #     print(r)
    # return max(len(n) for n in dp[-1])


T = int(input())
for t in range(T):
    ans = solve()
    print("Case #{}: {}".format(t+1, ans))
