# https://open.kattis.com/problems/8queens

def solve():
    g = []

    count = 0
    for i in range(8):
        g.append(input())

    for r in range(8):
        for c in range(8):
            if g[r][c] == '*':
                count += 1
                if check(g,r,c) == False:
                    return False

    if count != 8:
        return False
    return True

def check(g,r,c):
    for r2 in range(8):
        for c2 in range(8):
            if g[r2][c2] == '*':
                if r != r2 and c == c2:
                    return False
                if c != c2 and r == r2:
                    return False
                if abs(r-r2) != 0 and abs(r-r2) == abs(c-c2):
                    return False
    return True

if (solve()):
    print("valid")
else:
    print("invalid")