def almostDifference(nums):

	# Stores frequencies of previous numbers
	ht = {}
	result = 0
	prefix_sum = 0

	# y is nums[i], x is all elements before it
	for i, n in enumerate(nums):
		
		# Calculate standard difference
		ht.setdefault(n, 0)
		result -= prefix_sum	# subtract all previous elements
		result += n*i			# add y i times for each of the i previous elements

		# Modify for "almost difference"
		ht.setdefault(n-1, 0)
		ht.setdefault(n+1, 0)
		result -= ht[n-1]*1		# remove the bonus (+)
		result -= ht[n+1]*-1	# remove the bonus (-)

		ht[n] += 1
		prefix_sum += n

	return result


_ = int(input())
nums = [int(x) for x in input().split()]
print(almostDifference(nums))