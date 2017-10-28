#!/bin/python3

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        # In dp[i], we store (j, k): k sequences of longest-length j ending at index i
        dp = [(1,1) for j in range(n)]
        longest = 1

        for i, val in enumerate(nums):
            curr_longest = 1
            count = 0
            # which of the previous subsequences can we extend with nums[i]?
            for j in range(i):
                if nums[j] < val:
		    # finds next value in subsequence
                    if dp[j][0] == curr_longest:
                        count += dp[j][1]
                    if dp[j][0] > curr_longest:
                        count = dp[j][1]

            # update dp for element i
            dp[i] = (curr_longest, max(dp[i][1], count))
            longest = max(longest, curr_longest)

        # how many of the longest subsequences are there?
        return sum(j[1] for j in dp if j[0] == longest)


        
                              

sol = Solution()
inp = [8,1,0,3,9,5,2,4,7,0,10,6,9,2]
#inp = [1, 3, 5, 4, 9]
r = sol.findNumberOfLIS(inp)

print(r)


fin.close()
fout.close()
