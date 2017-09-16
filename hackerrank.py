#!/bin/python3


class Solution(object):
	def find132pattern(self, nums):
		"""
		:type nums: List[int]
		:rtype: bool
		"""
		n = len(nums)
		if n <= 2:
			return False    
		p_ind = 0
		pairs = []
		for a in range(1, n):
			if (nums[a-1] >= nums[a]):        # add pair with largest difference --> endpoints of increasing slope
				if (p_ind < a-1):
					pairs.append([nums[p_ind], nums[a-1]])
				p_ind = a
			for p in pairs:
				if (nums[a] > p[0] and nums[a] < p[1]):
					return True  
		print(pairs)
		return False
                              

sol = Solution()
inp = [3,1,4,2]
r = sol.find132pattern(inp)

print(r)
