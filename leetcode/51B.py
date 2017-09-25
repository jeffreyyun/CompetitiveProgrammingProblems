
#!/bin/python3


class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        time = [d for d in time if d != ':']
        digits = sorted([d for d in time])

        # set digit to larger allowed digit, else set it to lowest allowed digit
        for d in range(3,-1,-1):
            print(digits, time)
            for c in digits:
                if c > time[d]:
                    time[d] = c
                    if int(''.join(time[2:])) < 60 and int(''.join(time[:2])) < 24:
                        return time[0]+time[1]+':'+time[2]+time[3]
                    else:
                        time[d] = digits[0]
                        break
            time[d] = digits[0]

        return time[0]+time[1]+':'+time[2]+time[3]



sol = Solution()
inp = "23:59"
r = sol.nextClosestTime(inp)

print("RETURN:", r)

