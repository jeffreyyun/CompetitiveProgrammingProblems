#!/bin/python3
import math
import copy
import time
from collections import Counter

def printParens(n):

    # Base Case and Build approach
    if n <= 0:
        return set()
    if n == 1:
        return set(['()'])
    oldSet = printParens(n-1)
    newSet = set()
    for p in oldSet:
        for cand in ['('+p+')', '()'+p, p+'()']:
            if cand not in newSet:
                newSet.add(cand)
    return newSet


def printParens2(n):

    # Constructive approach, based on CtCC solution
    def addParen(r,l,wip):
        if r == 0 and l == 0:
            resSet.add(wip)
        elif r < l or l < 0: # invalid
            return
        else:
            addParen(r-1, l, wip+")")
            addParen(r, l-1, wip+"(")

    resSet = set()
    addParen(n, n, "")
    return resSet


def test(inp):
    print("-----TESTING BEGINS-----")
    res = printParens2(inp)
    print(res)
    return res

inps = [3]

for inp in inps:

    start_time = time.time()
    test(inp)
    t1 = time.time() - start_time

    # start_time = time.time()
    # test(inp)
    # t2 = time.time() - start_time

    # test(t1/t2)