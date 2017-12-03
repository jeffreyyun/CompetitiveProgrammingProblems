class Solution:
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        N = len(temperatures)
        ans = [0 for i in range(N)]
        for i in range(N-2, -1, -1):
            if temperatures[i] < temperatures[i+1]:
                ans[i] = 1
            else:
                if ans[i+1] == 0:
                    ans[i] = 0
                else:
                    # Follow the chain of succeeding temperatures
                    curr = ans[i+1] + i
                    while temperatures[curr] <= temperatures[i]:
                        # print(i, curr)
                        if ans[curr] == 0 or curr >= N:
                            curr = i
                            break
                        curr += ans[curr]
                    ans[i] = curr - i
        return ans
