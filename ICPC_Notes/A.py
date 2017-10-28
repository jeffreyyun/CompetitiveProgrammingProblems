# https://math.stackexchange.com/a/1367732/389053

# Find intersection points between two circles
# -- correct algorithm I think, but does not pass test cases

import sys
import math
from math import pow

FNAME = "A"
FNAME = "intersec"
###########
fin, fout = open(FNAME + ".in", "r"), open(FNAME + ".out", "w")
sys.stdin = fin
sys.stdout = fout
###########

EPS = 1e-7

def solve(ax, ay, ar, bx, by, br):
    if (ax == bx and ay == by and ar == br):
        print(3)    # same circle - inf intersections
        return

    dist_centers = math.sqrt((ax-bx)*(ax-bx) + (ay-by)*(ay-by))
    R = dist_centers
    if R == 0 and ar != br:
        print(0)    # no intersections
        return

    t1 = (ar*ar - br*br)/(2*R*R)
    cx = (ax+bx)/2 + t1*(bx-ax)
    cy = (ay+by)/2 + t1*(by-ay)

    t2a = 2*(ar*ar + br*br)/(R*R) - 4*t1*t1 - 1
    if (t2a < 0):
        print(0)    # no intersections
        return

    t2 = math.sqrt(t2a)/2
    dx = t2*(by - ay)
    dy = t2*(ax - bx)

    ix, iy = cx+dx, cy+dy
    jx, jy = cx-dx, cy-dy

    if (ix == jx and iy == jy) or abs(dist_centers - ar - br) < EPS:
        print(1)        # 1 intersection
        print(ix, iy)
    else:
        # want H, len(OH), len(HP)
        print(2)        # 2 intersection
        Hx = (jx + ix)/2
        Hy = (jy + iy)/2
        OH = math.sqrt(pow(Hx-ax, 2)+pow(Hy-ay, 2))
        HP = math.sqrt(pow(Hx-ix, 2)+pow(Hy-iy, 2))
        print(Hx, Hy)
        print(OH, HP)
        print(ix, iy)
        print(jx, jy)


TC = int(input())
for _ in range(TC):
    ax, ay, ar = [int(i) for i in input().split()]
    bx, by, br = [int(i) for i in input().split()]
    solve(ax, ay, ar, bx, by, br)


fin.close()
fout.close()
