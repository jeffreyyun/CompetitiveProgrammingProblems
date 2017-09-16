#!/bin/python3


fin = open('A.in', 'r')
fout = open('A.out', 'w')

class Solution(object):
	def integerBreak(self, num):
		"""
		:type n: int
		:rtype: int
		"""
		dp = [0 for i in range(num+1)]
		a = 1
		for n in range(num+1):

			a1 = pow(a,n//a-n%a) * pow(a+1,n%a)
			a2 = pow(a+1,n//(a+1)-n%(a+1)) * pow(a+2,n%(a+1)) if (n//(a+1) >> 1) else 0
			a += (a2 > a1)
			dp[n] = max(a1, a2)

		return dp[num]
        
                              

sol = Solution()
inp = 2
r = sol.integerBreak(inp)

print(r)

fin.close()
fout.close()
