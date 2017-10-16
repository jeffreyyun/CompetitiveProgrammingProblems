import collections

class Solution:
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 50000
        start = {}
        end = {}
        count = collections.Counter(nums)
        for i in range(len(nums)):
            # if nums[i] not in count:
            #     count[nums[i]] = 1
            # else:
            #     count[nums[i]] += 1
            # if nums[i] not in start:
            #     start[nums[i]] = i
            start.setdefault(nums[i],i)
            end[nums[i]] = i
        f = max(count.values())
        for i in count.keys():
            if count[i] == f:
                result = min(result, end[i]-start[i]+1)
        return result

sol = Solution()

inp = [1,2,2,3,1,4,2]

ppp = sol.findShortestSubArray(inp)

print(ppp)