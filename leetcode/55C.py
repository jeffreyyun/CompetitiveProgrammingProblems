class Solution:
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
	# Time: O(N^2)
	# Space: O(N)
	# Forums: could do two loops (finding longest contiguous set starting at every index) for O(1)
        subprods = {}
        total = 0
        for i in range(len(nums)):
            oldkeys = list(subprods.keys())
            for p in oldkeys:
                subprods[p] *= nums[i]
                if subprods[p] >= k:
                    del subprods[p]
                else:
                    total+=1
            if nums[i] < k:
                subprods[i] = nums[i]
                total+=1
        return total
