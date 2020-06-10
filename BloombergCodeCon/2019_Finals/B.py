#Problem        : Marathon
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

# Binary search on t O(30) for binary search

# for each t, will you qualify?
#

def qualifies(t, X):
    if t <= 0:
        return False
    # How many points are needed to qualify? Do you have that number?
    points = []
    for i in range(len(results)):
        pts = sum(int(a < t) for a in results[i] if a >= 0)    # all qualifying races
        points.append(pts)
    mypoints = points[0]
    points.sort(key = lambda x:-x)
    # print(mypoints, "need", points[X-1], points)
    return mypoints >= 1 and mypoints >= points[X-1]  # qualifies if at least as many point as X-th place
    
    
N, K, X = map(int, input().split())
results = []
if qualifies(1, X) and X >= N:
    print(1)
for _ in range(N):
    times = list(map(int, input().split()))
    results.append(times)
    
lo, hi = 1, 1e60 # hi TBD
while lo < hi:
    mid = int((lo + hi)//2)
    # print('lo{}, hi{}, mid{}'.format(lo, hi, mid))
    if qualifies(mid, X):  # works, so try lower time
        hi = mid
    else:   # doesn't work, so try higher time
        lo = mid + 1

q1, q2, q3, q4 = qualifies(lo-1, X), qualifies(lo, X), qualifies(lo+1, X), qualifies(lo+2, X)
# print(q1,q2,q3,q4)
# ERROR: looks like something was falsely marked as impossible...
if not q1 and not q2 and not q3 and not q4:
    print('IMPOSSIBLE')
elif q1:
    assert(not qualifies(lo-2, X))
    print(lo-1)
elif q2:
    print(lo)
elif q3:
    print(lo+1)
elif q4:
    print(lo+2)
else:
    for i in range(lo+2):
        if qualifies(i, X):
            res = i
            break
    print(res)
