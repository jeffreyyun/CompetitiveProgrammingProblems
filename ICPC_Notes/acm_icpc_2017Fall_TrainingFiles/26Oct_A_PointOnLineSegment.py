import sys

FNAME = "point"
###########
fin, fout = open(FNAME + ".in", "r"), open(FNAME + ".out", "w")
sys.stdin, sys.stdout = fin, fout
###########

tx, ty, ax, ay, bx, by = [float(u) for u in input().split()]

if tx >= min(ax,bx) and tx <= max(ax,bx) and ty >= min(ay,by) and ty <= max(ay,by):
    if (ax == bx):
        if (ax == tx):
            print("YES")
        else:
            print("NO")
    elif (ay == by):
        if (ay == ty):
            print("YES")
        else:
            print("NO")
    elif (tx-ax)/(bx-ax) == (ty-ay)/(by-ay):
        print("YES")
    else:
        print("NO")
else:
    print("NO")

fin.close()
fout.close()
