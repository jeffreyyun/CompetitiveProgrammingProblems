class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        sums = [0 for i in range(n-k+1)]
        mleft = [0 for i in range(n-k+1)]
        mright = [0 for i in range(n-k+1)]

        # Use DP to get sums of subsets
        for i in range(0, k):
            sums[0] += nums[i]

        for i in range(1, n-k+1):
            sums[i] = sums[i-1]-nums[i-1]+nums[i+k-1]

        # Use DP to find max sum in left and right intervals
        mleft[0] = (sums[0], 0)
        for i in range(1, n-2*k+1):
            if sums[i] > mleft[i-1][0]:
                mleft[i] = (sums[i], i)
            else:
                mleft[i] = mleft[i-1]

        mright[n-k] = (sums[n-k], n-k)
        for i in range(n-k-1, 2*k-1, -1):
            if sums[i] > mright[i+1][0]:
                mright[i] = (sums[i], i)
            else:
                mright[i] = mright[i+1]

        # Use DP to find middle interval (i - middle interval's starting index)
        ans = (0,0,0,0)
        #print(sums, mleft, mright)
        for i in range(k, n-2*k+1):       # goes from left to guarantee lexicographic ordering
            trisum = mleft[i-k][0] + sums[i] + mright[i+k][0]
            if trisum > ans[0]:
                ans = (trisum, mleft[i-k][1], i, mright[i+k][1])

        return [ans[1],ans[2],ans[3]]


sol = Solution()

nums = [1,9,16,14,13,18,18,9,1,17,6,3,8,2,20,16,10,17,19,3,8,14,11,19,8,19,18,1,14,7,17,8,16,15,9,5,11,11,9,18]
k = 12

ppp = sol.maxSumOfThreeSubarrays(nums, k)

print(ppp)