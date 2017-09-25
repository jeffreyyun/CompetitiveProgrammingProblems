#!/bin/python3


class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        result = 0

        for op in ops:

            if op == "C":
                stack.pop();
            elif op == "D":
                stack.append(stack[-1]*2)
            elif op == "+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(op))

        for s in stack:
            result += s
        return result



sol = Solution()
inp = ["5","2","C","D","+"]
r = sol.calPoints(inp)

print(r)

