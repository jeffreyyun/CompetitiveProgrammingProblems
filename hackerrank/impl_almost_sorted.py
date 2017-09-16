# Category: Algorithms - Implementation
# Difficulty: Medium

#!/bin/python3

def swapcheck(A, S, N):
	# find two indexes which are not in the right places
	swap1 = 0
	swap2 = N - 1

	while swap1 < N and A[swap1] == S[swap1]:
		swap1 += 1
	while swap2 >= 0 and A[swap2] == S[swap2]:
		swap2 -= 1

	A[swap1], A[swap2] = A[swap2], A[swap1]
	if A == S:
		print("yes")
		print("swap", swap1+1, swap2+1)	# output uses 1-indexing
		return True
	else:
		A[swap1], A[swap2] = A[swap2], A[swap1] # undo the swap

		# checks for reverse
		sub = A[swap1:swap2+1]
		sub.reverse()
		A[swap1:swap2+1] = sub
		if A == S:
			print("yes")
			print("reverse", swap1+1, swap2+1) # output uses 1-indexing
			return True
		else:
			return False

def main():

	N = int(input())
	A = [int(x) for x in input().split()]

	S = A[:]
	S.sort()

	if swapcheck(A, S, N):
		return
	print("no")

if __name__ == '__main__':
	main()