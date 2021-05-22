# Time: O(N)
# Space: O(N)

T = int(input())

for t in range(T):
    N, K = map(int, input().split())
    S = input()

    goodness = 0
    for i in range(N//2):
        goodness += (S[i] != S[-(i+1)])

    ans = abs(K - goodness)
    print(f"Case #{t+1}: {ans}")
