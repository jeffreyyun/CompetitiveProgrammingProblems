class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Time: O(N^2)
        res = 0
        for i in range(len(s)):
            k = 1
            while i-k >=0 and i+k < len(s) and s[i-k]==s[i+k]:
                k += 1
            res = max(res, k*2-1)
            k = 1
            while i-k >= 0 and i+k-1 < len(s) and s[i-k]==s[i+k-1]:
                k += 1
            res = max(res, k*2-2)
        return res


s = "bbbab"
sol = Solution()
res = sol.longestPalindromeSubseq(s)
print(res)
