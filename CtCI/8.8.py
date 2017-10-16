#!/bin/python3
import math
import copy
import time
import numpy as np
from collections import Counter

def subPerm(s):
    # Set-based approach
    if len(s) <= 0:
        return set()
    if len(s) == 1:
        return set(s)
    oldSet = subPerm(s[1:])
    newSet = set()
    size = len(s)
    for perm in oldSet:
        for pos in range(size):
            cand = perm[:pos]+s[0]+perm[pos:]
            # set data structure automatically prevents duplicates
            # but checking improves runtime
            if cand not in newSet:
                newSet.add(perm[:pos]+s[0]+perm[pos:])
    return newSet

def subPerm2(s):
    # CtCC solution (much faster if many duplicates)
    cnt = Counter(s)
    rSet = set()

    def helper(pref, remaining, rSet):
        # Base case. Permutations completed
        if (remaining == 0):
            rSet.add(pref)
            return
        # Try remaining letters for the next char
        # Generate permutations for each
        for c in cnt:
            if (cnt[c] > 0):
                cnt[c] -= 1
                helper(pref + c, remaining - 1, rSet)
                cnt[c] += 1

    helper("", len(s), rSet)
    return rSet

def numOfPerms(s):
    N = len(s)
    cnt = Counter(s)
    denom = 1
    for c in cnt:
        if cnt[c] >= 2:
            denom *= math.factorial(cnt[c])
    ans = math.factorial(N)/denom
    return ans


inps = ["aaaaabbbbbaaaaa", "aaaaaccccc", "aaaaaccbbb", "aaaacbbbbcaaaa", "abcdejjj", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"]

for inp in inps:

    start_time = time.time()
    subPerm(inp)
    t1 = time.time() - start_time

    start_time = time.time()
    subPerm2(inp)
    t2 = time.time() - start_time

    print(t1/t2, numOfPerms(inp))
