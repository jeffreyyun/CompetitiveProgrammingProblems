class Solution:
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        comp = sorted(arr)
        # Traverse from left, checking of set so far is our desired set
        start = 0
        end = 1
        chunks = 0
        countComp = {}
        countCurr = {}
        lastSeen = {}
        for i, c in enumerate(arr):
            lastSeen[c] = i
        # If count is same, we can split it into a chunk
        while end <= len(arr):
            countCurr.setdefault(arr[end-1], 0)
            countComp.setdefault(comp[end-1], 0)
            countCurr[arr[end-1]] += 1
            countComp[comp[end-1]] += 1
            # if the count of the two lists are the same
            # and elements of arr will not be seen again
            if countCurr == countComp:
                # print(start, end, countComp, countCurr)
                # This char will appear later, so we cannot split into chunk
                check = True
                endC = max(arr[start:end])
                for c in set(arr[start:end-1]):
                    if lastSeen[c] >= end and c != endC:
                        # print(c, endC)
                        check = False
                if check == False:
                    end += 1
                    continue
                chunks += 1
                start = end
                countComp = {}
                countCurr = {}
            end += 1
        return chunks


sol = Solution()
arr = [0,0,1]

res = sol.maxChunksToSorted(arr)
print(res)
