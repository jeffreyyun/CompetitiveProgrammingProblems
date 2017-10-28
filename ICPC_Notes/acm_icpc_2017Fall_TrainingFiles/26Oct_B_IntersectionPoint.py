import sys

FNAME = "A"
#FNAME = "intersec"
###########
#fin, fout = open(FNAME + ".in", "r"), open(FNAME + ".out", "w")
#sys.stdin = fin
#sys.stdout = fout
###########

a1, b1, c1, a2, b2, c2 = [int(i) for i in input().split()]
c1, c2 = -c1, -c2

if b1 == 0:
    x = c1/a1
    y = (c2 - a2*x)/b2

if b2 == 0:
    x = c2/a2
    y = (c1 - a1*x)/b1

if b1 != 0 and b2 != 0:
    num = c2/b2 - c1/b1
    den = a2/b2 - a1/b1
    x = num/den
    y = (c1 - a1*x)/b1

print(x, y)
