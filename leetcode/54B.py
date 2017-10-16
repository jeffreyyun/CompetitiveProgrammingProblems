class Solution:
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count, prev_c, curr_c = 0,0,0
        curr = s[0]
        for c in s:
            if c == curr:
                # add to the streak
                curr_c += 1
            else:
                # switches off to next char
                count += min(prev_c, curr_c)
                prev_c = curr_c
                curr_c = 1
                curr = c
        count += min(prev_c, curr_c)
        return count

sol = Solution()

inp = "00110011"

ppp = sol.countBinarySubstrings(inp)

print(ppp)