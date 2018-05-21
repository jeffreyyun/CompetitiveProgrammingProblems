import math

class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        """
        Find n s.t. 1+...+n >= target
        Smallest n for above found with Quadratic (n^2 + n - 2*target = 0)
        """
        n = math.ceil((-1 + math.sqrt(1 + 8*abs(target)))/2)
        summed = n*(n+1)/2

        diff = summed - target 
        # If diff == 0, return n
        # If diff is even, just flip an x in [1, n] (go -x steps instead of x steps)
        # If diff is odd, and n+1 is odd, add n+1 to summed to make it even
        # If diff is even, and n+1 is even, subtract n+1 and add n+2 to summed to make it even
        if diff % 2 == 0:
            return n                    # namely flip diff/2
        else:
            if (n + 1) % 2 == 1:        # add n+1
                return n + 1            # then flip (diff+n+1)/2
            else:                       # sub n+1, add n+2
                return n + 2            # then flip (diff+1)/2


# def reachNumber(self, target):
#     # Parity
#     count = 0

#     for i in range(888888):
#         count += i

#         if abs(target) <= abs(count) and target % 2 == count % 2:
#             return i


sol = Solution()
for target in range(-100, 100):
    result = sol.reachNumber(target)
    print(target, result)