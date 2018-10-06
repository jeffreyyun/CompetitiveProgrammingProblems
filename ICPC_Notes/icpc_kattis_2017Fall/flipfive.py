# https://open.kattis.com/problems/flipfive


import copy

def solve(memo, target):
    stringified = ''.join(target)
    return memo[stringified]



def setup(memo, grid):
    # setups the memo completely
    stringified = ''.join(grid)
    memo[stringified] = 0
    count = 0
    newg, prevg = [],[stringified]
    while True:
        count += 1
        # store grids
        for g in prevg:
            stringified = ''.join(g)
            for r in range(3):
                for c in range(3):
                    # try this flip
                    an = flip(g,r,c)
                    san = ''.join(an)
                    if san not in memo:
                        newg.append(san)
                        memo[san] = count
        if len(newg) == 0:
            break
        prevg = copy.copy(newg)
        newg = []


def flip(g,r1,c1):
    g = list(g)
    an = copy.copy(g)
    for r in range(3):
        for c in range(3):
            i = r*3+c
            if abs(r-r1)+abs(c-c1)==1 or abs(r-r1)+abs(c-c1)==0:
                if g[i] == '*':
                    an[i] = '.'
                else:
                    an[i] = '*'
            else:
                an[i] = g[i]
    return an



T = int(input())
memo = {}
start = ['.','.','.','.','.','.','.','.','.']
setup(memo, start)


for _ in range(T):
    g = []
    for r in range(3):
        cici = input()
        for c in cici:
            g.append(c)
    ans = solve(memo, g)
    print(ans)