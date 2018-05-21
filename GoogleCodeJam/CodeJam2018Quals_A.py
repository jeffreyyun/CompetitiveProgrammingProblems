"""
Naive works
O(P^3) complexity

while 'CS' exists (going right to left):
    swap to 'SC'
    simulate to see if falls under damage

"""

def adjust(P):
    """ swaps two commands in P """
    for i in range(len(P)-2, -1, -1):       # easily change to O(P^2) by keeping track of i
        if P[i] == 'C' and P[i+1] == 'S':
            P[i], P[i+1] = P[i+1], P[i]
            return True
    return False

def simulate(P):
    damage = 0
    power = 0
    for c in P:
        if c == 'C':
            power += 1
        else:
            damage += 1 << power
    return damage

def solve():
    D, P = input().split()
    D = int(D)
    P = list(P)

    count = 0
    while simulate(P) > D and adjust(P):
        count += 1

    if simulate(P) <= D:
        return count
    else:
        return "IMPOSSIBLE"


T = int(input())
for _ in range(T):
    ans = solve()
    print("Case #{}: {}".format(_+1, ans))
