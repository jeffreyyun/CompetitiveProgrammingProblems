#Problem        : Spot Two Differences
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()
A, N, B = map(int, [data[0], data[2], data[3]])

def differ(N, a, b):
    diff = sum(a[i] != b[i] for i in range(N))
        if diff > 2:
            return False
    return diff == 2
   
def solve(): 
    words = list(set(data[4:]))
    ans = 0
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            if differ(N, words[i], words[j]):
                ans += 1
    print(ans)

if N == 1:
    print(0)
else:
    solve()
    