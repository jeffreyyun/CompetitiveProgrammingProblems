class Solution:
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        memoyes = [0 for i in range(10000)]
        memono = [0 for i in range(10000)]

        def choose():
            for i in range(1,10000):
                memoyes[i] = memono[i-1] + sums[i]
                memono[i] = max(memoyes[i-1], memono[i-1])
            return

        sums = [0 for i in range(10000)]
        for n in nums:
            sums[n] += n
        choose()
        return max(max(memoyes), max(memono))
