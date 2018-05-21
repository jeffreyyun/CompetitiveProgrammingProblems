class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        # Traverse from left, checking of set so far is our desired set
        start = 0
        end = 1
        chunks = 0
        while end <= len(arr):
            if set(arr[start:end]) == set(range(start, end)):
                chunks += 1
                start = end
            end += 1
        return chunks


sol = Solution()
arr = [0,1,2,3,4,5,6,7,8,9]

res = sol.maxChunksToSorted(arr)
print(res)
