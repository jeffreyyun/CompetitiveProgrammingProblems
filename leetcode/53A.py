import math

class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ans = n^(n>>1)
        lg = (1<<int((math.log(n,2)//1 + 1))) - 1       # (next power of 2 higher than n) - 1
        return (ans == lg)


sol = Solution()

for inp in range(1,20):
    ppp = sol.hasAlternatingBits(inp)
    print(ppp)