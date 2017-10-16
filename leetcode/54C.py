class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        print(sorted(nums), sum(nums))
        each_sum = sum(nums)/k
        if int(each_sum) != each_sum or max(nums) > each_sum:
            return False
        if k == 1:
            return True
        return True


sol = Solution()

inp = [1, 2, 2, 2, 3, 3, 3, 4, 4, 6, 7, 7, 8, 8, 9, 9]

ppp = sol.canPartitionKSubsets(inp, 6)

print(ppp)