# Time: O(N^2 log N^2 + N^2)
# Space: O(N^2)

T = int(input())

for t in range(T):
    N, Q = map(int, input().split())

    # for loops are expensive --> use list comprehensions
    nums = list(map(int, input().split()))
    for i in range(1, N):
        nums[i] += nums[i-1]
    nums = [0] + nums

    # forms sums of subsets
    sums = [nums[j]-nums[i] for i in range(N+1) for j in range(i+1, N+1)]
    sums.sort()
    sumsLen = N*(N+1)//2
    for i in range(1,sumsLen):
        sums[i] += sums[i-1]
    sums = [0] + sums

    print("Case #{}:".format(t+1))
    for q in range(Q):
        a, b = map(int, input().split())
        print(sums[b] - sums[a-1])
