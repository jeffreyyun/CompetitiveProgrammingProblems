#Problem        : Volleyball Rotations
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys
import queue

data = sys.stdin.read().splitlines()

N = int(data[0])
setter = data[1] #string
start = data[2].split()
sidelines_no, sidelines = data[3][0], data[3][2:].split()

on = queue.Queue()
off = queue.Queue()
for i in sidelines:
    off.put(i)
for i in [1,2,3,4,5,0]:
    # adhere by the strange layout given by the problem
    on.put(start[i])

for i in range(N):
    # take a person off; if setter, return them; if not, bring on the next person
    p = on.get()
    if p == setter:
        on.put(p)
    else:
        pnew = off.get()
        #print(pnew, "is on and",p,"is off" )
        on.put(pnew)
        off.put(p)

end = []
while not on.empty():
    end.append(on.get())

ans = []
for i in [5,0,1,2,3,4]:
    ans.append(end[i])

print(' '.join(ans))