#!/bin/python3
import time
import math
import queue
import collections
from collections import Counter


class Solution(object):
    def __init__(self):
        pass

    def FUNCTION(self):
        return "Hello ICPC"


sol = Solution()
inp = [1,0,1,3,4,7]
ppp = sol.FUNCTION(inp)
print(ppp)


inps = ["Hello"]

for inp in inps:
    start_time = time.time()
    test(inp, 1)
    t1 = time.time() - start_time
    print(t1)



fin = open('A.in', 'r')
fout = open('A.out', 'w')
fin.close()
fout.close()
