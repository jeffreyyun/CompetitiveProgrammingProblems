class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        def isSelfDividing(num):
            s = str(num)
            for digit in s:
                if int(digit) == 0 or i % int(digit) != 0:
                    return False
            return True

        ans = []
        for i in range(left, right+1):
            if isSelfDividing(i):
                ans.append(i)

        return ans
