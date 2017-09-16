#!/bin/python3


fin = open('A.in', 'r')
fout = open('A.out', 'w')

# class Solution(object):
#     def findLengthOfLCIS(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         n = len(nums)
#         if n <= 1:
#             return n
#         curr = nums[0]
#         res = 0
#         temp = 1
#         for i in range(n):
#             if nums[i] > curr:      # if increasing, add to sequence
#                 temp += 1
#                 curr = nums[i]
#             else:                   # start new sequence
#                 if temp > res:
#                     res = temp
#                 curr = nums[i]
#                 temp = 1

#         if temp > res:
#             res = temp
#         return res
        

# More elegant (wrote half hour after looking at forum)
class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 1
        i = 0
        while i < len(nums):
            curr_longest = 1
            while i+1 < len(nums) and nums[i+1] > nums[i]:
                i += 1
                curr_longest += 1
            longest = max(longest, curr_longest)
            i += 1
        return longest        
                              

sol = Solution()
inp = [1,0,1,3,4,7]
r = sol.findLengthOfLCIS(inp)

print(r)


fin.close()
fout.close()