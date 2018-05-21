def printMatrix(M):
    for r in M:
        print(r)

def generate(N, A1, B1, C, D, E1, E2, F):
    A = [0]*N
    B = [0]*N
    x = [0]*N
    y = [0]*N
    r = [0]*N
    s = [0]*N
    A[0], B[0], x[0], y[0] = A1, B1, A1, B1
    for i in range(1, N):
        x[i] = (C*x[i-1]+D*y[i-1]+E1) % F
        y[i] = (D*x[i-1]+C*y[i-1]+E2) % F
        r[i] = (C*r[i-1]+D*s[i-1]+E1) % 2
        s[i] = (D*r[i-1]+C*s[i-1]+E2) % 2
        A[i] = (-1)**r[i] * x[i]
        B[i] = (-1)**s[i] * y[i]

    # Multiply A and B
    M = [[0 for _ in range(N)] for __ in range(N)]
    for i in range(N):
        for j in range(N):
            M[i][j] = A[i]*B[j]

    print(x, y, A, B)
    printMatrix(M)
    return M

def getSubmatrixSum(N, K, M):
    result = 0

    return result


T = int(input())

for t in range(T):
    N, K, A1, B1, C, D, E1, E2, F = map(int, input().split())
    M = generate(N, A1, B1, C, D, E1, E2, F)

    result = getSubmatrixSum(N, K, M)
    print("Case #{}: {}".format(t+1, result))
