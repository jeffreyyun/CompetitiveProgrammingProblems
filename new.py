#!/bin/python3
import math

def dist(p1, p2):
    d = math.sqrt((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)
    return d

def processSinglePoint(i1, count):
    global P, count
    for i2 in range(i1+1, P):
        p1, p2 = pts[i1], pts[i2]
        diff = p2[0] - p1[0]
        if diff < -2018:
            continue
        elif diff > 2018:
            return
        else:
            if dist(p1, p2) == 2018.0:
                count += 1

count = 0
P = int(input())
pts = []
for pt in range(P):
    x1, y1 = [int(i) for i in input().split()]
    pts.append((x1, y1))
pts.sort()

for i1 in range(P):
    processSinglePoint(i1, count)

print(count)

# print(pts)

# ans = []
# for i in range(P):
#     for j in range(i+1,P):
#         ans.append(dist(pts[i], pts[j]))
# print([int(i) for i in ans])