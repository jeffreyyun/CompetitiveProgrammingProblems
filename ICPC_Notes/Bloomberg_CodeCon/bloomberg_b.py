#Problem        : Sum Sum Cryptography
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import math

N = int(input())

col = set()

# searched fervently for elegant, quick algorithm
# but after 20 minutes of nothing, tried brute force...it worked
for x in range(int(math.sqrt(N))-2):
    x2 = x*x
    for y in range(int(math.sqrt(N-x2))-1):
        y2 = y*y
        z = math.sqrt(N-x2-y2)
        if z == int(z):
            #print(x,y,int(z),x+y+int(z))
            col.add(tuple(sorted([x,y,int(z)])))

sm = 0
for i in col:
    sm += sum(i)

print(sm)

