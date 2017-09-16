#!/bin/python2

# leetcode.com/contest/leetcode-weekly-contest-45 "Hard problem"
# IT'S A BASE-10 to BASE-9 CONVERTER, haha

class Solution(object):
    def newInteger(self, n, base):
        """
        :type n: int
        :rtype: int
        """
        ans = 0;
        mul = 1;
        while (n > 0):
            print(ans, mul)
            ans += mul * (n % base);
            mul *= 10;
            n /= base;
        return ans;

i = int(input())
s = Solution()
print(s.newInteger(i, 9))
