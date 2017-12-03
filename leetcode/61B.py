class Solution:
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        N = list(str(N))
        good = False
        while not good:
            good = True
            for i in range(1, len(N)):
                if N[i] < N[i-1]:
                    if N[i] != '0':
                        N[i] = str(int(N[i]) - 1)
                    else:
                        N[i-1] = str(int(N[i-1]) - 1)
                        N[i] = '9'
                    for j in range(i+1, len(N)):
                        N[j] = '9'
                    good = False
                    break
        ans = ''.join(N[1:])
        ans = str(N[0]) + ans if N[0] != '0' else ans
        return int(ans)
