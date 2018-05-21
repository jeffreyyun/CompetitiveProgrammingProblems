class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        count = 0
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31}
        for i in range(L, R+1):
            count += bin(i).count('1') in primes

        return count







        
sol = Solution()
L = 10
R =15

res = sol.countPrimeSetBits(L,R)
print(res)

