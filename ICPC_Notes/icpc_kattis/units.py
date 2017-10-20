# https://open.kattis.com/contests/tda3e4/problems/units
# Implementation Incomplete

import copy

U = int(input())

while U != 0:
    units = input().split()
    bases = {}
    rels = {}
    for _ in range(U-1):
        r = input().split(' ')
        rels[(r[0],r[3])] = int(r[2])
        # rels[(km,m)]=1000

    smallest, prev_smallest = [],[]
    isBase = {}
    for r in rels.keys():
        isBase{r[0]} = False
        isBase.setdefault(r[1], True)
    while len(smallest) != 1:
        prev_smallest = copy.copy(smallest)
        for u in units:
            if u in smallest:
                smallest.append(u)
    for u in smallest:      # only one element!!!
        bases[u] = 1
        isBase[u] = True

    for r in rels.keys():
        print(r,rels[r])
        if r[1] == smallest:
            bases[r[0]] = rels[r]

    change = True
    while change:
        change = False
        comps = list(bases.keys())
        for b in comps:
            for r in rels.keys():
                if r[1] == b and r[0] not in bases:
                    print(r[0], rels[r], bases[r[1]])
                    bases[r[0]] = rels[r]*bases[r[1]]
                    change = True
                elif r[0] == b and r[1] not in bases:
                    bases[r[1]] = bases[r[0]]/rels[r]
                    change = True


    ordered = [(bases[units[i]],units[i]) for i in range(U)]
    ordered.sort()
    print("ordered",ordered)





    U = int(input())
