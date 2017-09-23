import sys

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s)-1
        while (i < j):
        	if s[i] != s[j]:
        		break
        	i,j = i+1,j-1
        try1 = s[:i]+s[i+1:]
        try2 = s[:j]+s[j+1:]
        return try1==try1[::-1] or try2==try2[::-1]

    # go from end

sol = Solution()
inp = "aba"
r = sol.validPalindrome(inp)

print(r)
