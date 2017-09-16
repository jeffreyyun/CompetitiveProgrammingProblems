# Category: Algorithms - Implementation
# Difficulty: Medium

#!/bin/python3

"""
Explanation:

The key here is we can only swap two balls,
so each container has the same amount of balls throughout.

In other words,
the Number of balls in each Bin have bijection with Number of balls of each Type.

So we sum them up into two arrays and compare the two, thus determining our answer.
"""

T = int(input())
for t in range(T):

	N = int(input())
	row_sums = [0]*N
	col_sums = [0]*N

	for i in range(N):
		contents = [int(e) for e in input().split()]
		for j in range(N):
			row_sums[i] += contents[j]
			col_sums[j] += contents[j]

	row_sums.sort()
	col_sums.sort()
	
	print("Possible" if row_sums == col_sums else "Impossible")