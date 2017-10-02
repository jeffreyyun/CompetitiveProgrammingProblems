class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # can we sort?

        # BRUTE FORCE counting
        ht = [0]*10008
        for i in range(len(nums)):
            if ht[nums[i]-1] == 1:
                dup = nums[i]
            else:
                ht[nums[i]-1] = 1
        for i in range(len(ht)):
            if ht[i] == 0:
                return [dup, i+1]

        # bonus technique from forums
        # Objective: Solve for duplicate and missing (x and y)
        N = len(nums)
        # sum(nums) = sum(1+2+...+N) + x - y
        xMy = sum(nums) - N*(N+1) / 2
        # sum(each num squared) = sum(1+4+...+N*N) + x*x - y*y
        xPy = (sum(x*x for x in nums) - N*(N+1)*(2*N+1) / 6) / xMy
        return [(xMy+xPy)/2, (xMy-xPy)/2]
