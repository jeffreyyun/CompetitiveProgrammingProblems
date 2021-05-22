import functools

N = int(input())

def solve(N):
    dp = [1, 1, 0, 0, 1, 1]
    if N < len(dp):
        return bool(dp[N])

    curr = True
    currNum = len(dp)
    repNum = 3
    while currNum <= N:
        curr = not curr # start False 3
        currNum += repNum
        repNum += int(curr) # if true, next time we +1 with False
    return curr

ans = solve(N)

print('YES' if ans else 'NO')