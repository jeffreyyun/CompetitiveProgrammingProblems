class Solution(object):
    def numSubarrayBoundedMax(self, A, L, R):
        """
        :type A: List[int]
        :type L: int
        :type R: int
        :rtype: int
        """
        a = 0
        res = 0
        count = 0
        mx = L
        for i in range(len(A)):
            mx = max(mx, A[i])
            if not L <= mx <= R:
                a = i+1
                count = 0
                mx = L
            # all previous subsets (there are count of them) can include A[i]
            elif A[i] < L:
                res += count
            else:
                count = i - a + 1
                res += count
        return res

sol = Solution()
A=[409,96,729,843,328,855,860,587,238,141,475,857,82,10,279,683,194,549,81,201,711,705,617,615,941,589,12,781,260,42,745,976,201,973,609,402,629,322,78,805,746,515,401,119,224,178,711,960,266,130,310,731,969,717,43,656,729,447,997,563,41,235,366,584,293,305,104,378,632,766,245,149,498,147,865,133,227,680,655,603,529,885,875,737,173,317,995,705,283,984,649,513,702,313,499,676,516,106,446,491]
L=542
R=772
res = sol.numSubarrayBoundedMax(A, L, R)
print(res)
