class Solution:
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """

        # DP - dp[i][j] store subproblem for s1[:i] and s2[:j] (up to (i-1)th char in s1, (j-1)th char in s2)
        n1, n2 = len(s1) + 1, len(s2) + 1
        dp = [[0 for j in range(n2)] for i in range(n1)]

        # initialize maximums
        for i in range(1, n1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        for j in range(1, n2):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        for i in range(1, n1):
            for j in range(1, n2):
                # do not delete these letters
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                # delete one or both letters
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))

        return dp[n1-1][n2-1]

sol = Solution()
s1="sjfqkfxqoditw"
s2="fxymelgo"
ppp = sol.minimumDeleteSum(s1,s2)
print(ppp)

