#Problem        : Hotshot
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()

L = int(data[0])
border = [tuple([int(x) for x in l.split()]) for l in data[1:L+1]]
OL = [int(x) for x in data[L+1].split()]
DL = [int(x) for x in data[L+2].split()]
bx, by = [int(x) for x in data[L+3].split()]

O = []
D = []
for i in range(0, 10, 2):
    O.append((OL[i], OL[i+1]))
    D.append((DL[i], DL[i+1]))

# print(L, OL, DL, bx, by)

def isBehindThree(mx, my):
    for i, p in enumerate(border):
        x, y = p
        if mx == x and my <= y:
            return False
    return True

def dist(mx, my, nx, ny):
    return (mx-nx)**2 + (my-ny)**2

max_from_defender = 0
res_from_defender = []
for mx, my in O:
    if isBehindThree(mx, my):
        my_dist = 99999999
        for nx, ny in D:
            my_dist = min(my_dist, dist(mx, my, nx, ny))      

        # print(mx, my, my_dist)  

        if my_dist > max_from_defender:
            max_from_defender = my_dist
            res_from_defender = [(mx, my)]
        elif my_dist == max_from_defender:
            res_from_defender.append((mx, my))

# print(res_from_defender)

min_from_ball = 99999999
res_from_ball = []
for mx, my in res_from_defender:
    # print(mx, my)
    my_dist = dist(mx, my, bx, by)
    if my_dist < min_from_ball:
        min_from_ball = my_dist
        res_from_ball = [(mx, my)]
    elif my_dist == min_from_ball:
        res_from_ball.append((mx, my))

# print(res_from_ball)

if len(res_from_ball) == 0:
    print("-1 -1")
else:
    res = [str(p[0]) + " " + str(p[1]) for p in res_from_ball]
    print(' '.join(res))