N, T = map(int, input().split())

potions = []

for _ in range(N):
    potions.append(int(input()))

potions.sort()

# last T, last 2*T, etc....
ans = all(p >= (i)*T+1 for i,p in enumerate(potions))

print('YES' if ans else 'NO')

