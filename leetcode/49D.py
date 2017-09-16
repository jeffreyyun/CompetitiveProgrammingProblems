#!/bin/python3


fin = open('A.in', 'r')
fout = open('A.out', 'w')

# Similar to DP
# class Solution(object):
#     def findNumberOfLIS(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         le = len(nums)
#         if le <= 1:
#             return le
#         # initializes - starting with nums[le-1] with its own subsequence of length 1
#         mhead = [[],[(le-1, 1)]]        # list of list of tuples -- (j, k) in m[a] corresponds to nums[j] starts k subsequences of length a
#         most = 1
#         for i in range(le-2, -1, -1):    # search nums from the end
#             temp = 0
#             found = False
#             for n in range(most, 0, -1):    # searches all subsequences of length n
#                 for j in mhead[n]:             # if nums[j[0]] > nums[i], nums[i] can head that nums[j[0]] subsequence
#                     if nums[j[0]] > nums[i]:   # compares values of indexes
#                         found = True
#                         temp += j[1]
#                 if found:
#                     if n+1 <= most:                 # add results into mhead
#                         mhead[n+1].append((i, temp))
#                     else:
#                         mhead.append([(i, temp)])   # longer subsequence found
#                         most += 1
#                     break
#             if not found:
#                 mhead[1].append((i, 1))             # subsequence of only itself

#         #print(mhead, most)
#         if (most == 1):
#             return le
#         return sum(j[1] for j in mhead[most])       # number of longest subsequences



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
                    if dp[j][0] == curr_longest:  # finds next value in subsequence
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