# Kickstart Round D 2017
# A: Go Sightseeing

"""
What I Learned
---------------
Debugging: Understand the base cases... does a cell start out as 0 or infinity?
"""

# Ts -- time_to_sightsee
# Tf -- time_to_finish
import math

def maxSightsee(N, Ts, Tf, start, freq, duration):
    def arrivalTime(i, j, sightsee):
        timeDone = prev[j] + Ts * int(sightsee) # when we start waiting
        timeDone = max(0, math.ceil((timeDone - start[i])/freq[i]))*freq[i] + start[i] # when we start leaving
        timeDone += duration[i] # when we arrive
        return timeDone

    # For i cities, check cost for sightseeing in 0...i cities
    curr = [1e12 for i in range(N)]
    curr[0] = 0
    for i in range(1, N):
        prev = curr
        curr = [1e12 for _ in range(N)]
        for j in range(i+1):
            curr[j] = min(arrivalTime(i-1, j-1, True), arrivalTime(i-1, j, False))
        # print("prev {}, curr{}".format(prev, curr))

    result = "IMPOSSIBLE"
    for i in range(N):
        if curr[i] <= Tf:
            result = i
        else:
            break
    return result


T = int(input())
for t in range(T):
    N, Ts, Tf = map(int, input().split())
    start, freq, duration = [0]*N, [0]*N, [0]*N
    for i in range(N-1):
        start[i], freq[i], duration[i] = map(int, input().split())
    result = maxSightsee(N, Ts, Tf, start, freq, duration)
    print("Case #{}: {}".format(t+1, result))
