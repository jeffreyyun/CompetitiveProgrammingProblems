X = int(input().split()[1])
Y = int(input().split()[1])
stairs = [[0 for _ in range(X)]]
for i in range(Y):
    stairs.append(list(map(int, input().split())))

dp_yes = [[0 for _ in range(X)] for __ in range(Y+1)]
dp_no = [[0 for _ in range(X)] for __ in range(Y+1)]

for i in range(1, Y+1):
    for j in range(X):
        dp_yes[i][j] = max(dp_yes[i-1][max(0, j-1):min(j+2,X)]) + stairs[i][j]
        dp_no[i][j] = max(max(dp_yes[i-1]), max(dp_no[i-1][max(0,j-1):min(j+2,X)])) + stairs[i][j]

result = max(dp_no[-1])
print(result)
