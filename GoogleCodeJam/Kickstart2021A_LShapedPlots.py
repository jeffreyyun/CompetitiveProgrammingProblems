T = int(input())

for t in range(T):
    R, C = map(int, input().split())
    matrix = []
    for _ in range(R):
        matrix.append(input().split())

    # Prefix sum on segments
    top = [[0]*C for _ in range(R)]
    bottom = [[0]*C for _ in range(R)]
    left = [[0]*C for _ in range(R)]
    right = [[0]*C for _ in range(R)]

    for i in range(R):
        left[i][0] = int(matrix[i][0] == '1')
        right[i][-1] = int(matrix[i][-1] == '1')
    for j in range(C):
        top[0][j] = int(matrix[0][j] == '1')
        bottom[-1][j] = int(matrix[-1][j] == '1')

    for i in range(R):
        for j in range(C):
            if matrix[i][j] != '1': continue
            if i != 0: top[i][j] = top[i-1][j] + 1
            if j != 0: left[i][j] = left[i][j-1] + 1
    for i in range(R-1, -1, -1):
        for j in range(C-1, -1, -1):
            if matrix[i][j] != '1': continue
            if i != R-1: bottom[i][j] = bottom[i+1][j] + 1
            if j != C-1: right[i][j] = right[i][j+1] + 1

    # getCountWithSegLengths
    def f(a, b):
        return max(0, min(a//2, b) - 1) + max(0, min(a, b//2) - 1)

    count = 0
    for i in range(R):
        for j in range(C):
            count += f(top[i][j], left[i][j]) + f(top[i][j], right[i][j]) + f(bottom[i][j], left[i][j]) + f(bottom[i][j], right[i][j])

    print(f"Case #{t+1}: {count}")
