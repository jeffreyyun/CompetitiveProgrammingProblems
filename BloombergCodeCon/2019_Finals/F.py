# #Problem        : Marathon
# #Language       : Python 3
# #Compiled Using : py_compile
# #Version        : Python 3.4.3
# #Input for your program will be provided from STDIN
# #Print out all output from your program to STDOUT

# # Binary search on t O(30) for binary search

# # for each t, will you qualify?
# #

# def qualifies(t, X):
#     if t <= 0:
#         return False
#     # How many points are needed to qualify? Do you have that number?
#     points = []
#     for i in range(len(results)):
#         pts = sum(int(a < t) for a in results[i] if a >= 0)    # all qualifying races
#         points.append(pts)
#     mypoints = points[0]
#     points.sort(key = lambda x:-x)
#     # print(mypoints, "need", points[X-1], points)
#     return mypoints >= 1 and mypoints >= points[X-1]  # qualifies if at least as many point as X-th place
    
# N, K, X = map(int, input().split())
# results = []
# maxT = 0
# for _ in range(N):
#     times = list(map(int, input().split()))
#     results.append(times)
#     maxT = max(maxT, max(times))

# res = 'IMPOSSIBLE'
# for i in range(maxT+2):
#     if qualifies(i, X):
#         res = i
#         break
# print(res)

#Problem        : Marathon
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

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
    return mypoints >= 1 and mypoints >= points[X-1]  # qualifies if at least as many point as X-th place
    
    
N, K, X = map(int, input().split())
results = []
maxT = 0
for _ in range(N):
    times = list(map(int, input().split()))
    results.append(times)
    maxT = max(maxT, max(times))

res = 'IMPOSSIBLE'
for i in range(maxT+2):
    if qualifies(i, X):
        res = i
        break
print(res)

