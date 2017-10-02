class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        total = len(s)
        n = len(s)
        for c in range(n):
            j = 1
            while (c-j+1 >= 0 and c+j < n and s[c-j+1] == s[c+j]):   # even length
                j += 1
                total += 1
            j = 1
            while (c-j >= 0 and c+j < n and s[c-j] == s[c+j]):       # odd length
                j += 1
                total += 1
        return total