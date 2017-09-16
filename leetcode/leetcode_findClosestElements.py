#!/bin/python3

# https://leetcode.com/contest/leetcode-weekly-contest-45/problems/find-k-closest-elements/

# find the k closest elements to x
def findClosestElements(a, k, x):
	b = sorted((abs(x-t), t) for t in a)	# simply sort by the absolute values
	# [(0, 1), (1, 0), (2, 3), (4, 5), (5, 6), (6, 7), (7, 8)]
	ans = sorted(i[1] for i in b[0:k])	# then take the first k!
	ans = sorted(map(lambda x: x[1], b[0:k]))
	# two ways to write the same thing
	return ans
	# [0, 1, 3]

a = {0,0,0,1,3,5,6,7,8,8}
k = 3
x = 1
print(findClosestElements(a,k,x))
