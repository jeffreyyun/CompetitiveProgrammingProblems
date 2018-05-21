class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        OPTIMAL SUBSTRUCTURE, OVERLAPPING SUBPROBLEMS

        dp[i] = length of LIS terminating at this #
        Once we know dp[0...i-1], we can find dp[i]

        Recurrence relation

        dp[i] = 1 + length of LIS belonging to num < nums[i]
        ==> 1 + max([dp[j] if nums[j] < nums[i] else 0 for j in range(i))
        """
        # DP with binary search (faster than above) - O(N log N)
        def search(i):
            toInsert = nums[i]
            lo = 0
            hi = length-1
            while lo <= hi:
                mid = lo + (hi-lo)//2
                try:
                    if nums[dp[mid]] > toInsert:
                        hi = mid-1
                    elif nums[dp[mid]] < toInsert:
                        lo = mid+1
                    else:   # if equal, then no need to insert
                        return -1
                except:
                    return -1

            # if smaller conclusion to IS of length (lo+1), replace dp[lo]
            if dp[lo] == -1 or toInsert < nums[dp[lo]]:
                return lo
            else:
                return -1 

        if len(nums) <= 1:
            return len(nums)

        # stores INDEX of smallest number terminating IS of this length
        dp = [-1]*len(nums)
        length = 0
        prev = [-1]*len(nums)     # if we want to actually find the LIS by backtracking

        for i in range(len(nums)):
            # Find where we would insert nums[i], considering elements in dp
            # Is nums[i] the smallest ending number for a subsequence of length (pos+1)?

            # e.g. nums = [10,9,2,5,3,7,101,18]
            # we would end with dp = [2,3,5,7] ==> e.g. IS of length 1 ends at index 2, length 4 ends at index 7
            pos = search(i)
            # It is.
            if pos != -1:
                dp[pos] = i
                prev[i] = dp[pos-1] if pos >= 1 else -1
                if pos == length:
                    length += 1

        # To recover LIS
        LIS = []
        ind = dp[length-1]
        while ind != -1:
            LIS.append(ind)
            ind = prev[ind] 
        LIS.reverse()

        # print(LIS)
        
        return length


sol = Solution()

tests = []
tests.append(([5,2,3,5,101,18],4))
tests.append(([1,2,1], 2))
tests.append(([77,82,84,80,398,286,40,136,162], 5))
tests.append(([1],1))
tests.append(([],0))
tests.append(([1,2,3,4,5,6,7,8,9,8], 9))


for *args, ans in tests:
    res = sol.lengthOfLIS(*args)
    print(res)
    assert(res==ans)