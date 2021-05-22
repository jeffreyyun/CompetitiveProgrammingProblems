# # 0/1 some won't work
# dp = {}
# curr = 7
# for i in range(10):
#     dp[curr] = 1
#     for k in list(dp.keys()):
#         dp[k+curr] = dp[k] + 1
#     curr += 10
# print(sorted(dp.keys()))

T = int(input())
d = [10,3,6,9,2,5,8,1,4,7]

for t in range(T):
    N = int(input())

    if N >= 70:
        print(d[N % 10])
    elif (N >= d[N % 10] * 7):
        print(d[N % 10])
    else:
        print(-1)
