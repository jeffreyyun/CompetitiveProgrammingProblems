from copy import deepcopy
class Solution:
    def break_expr(self, expression):
        # print("break_expr was given: ", expression)
        cmds = []
        # remove main parentheses, if any
        if expression[0] == '(' and expression[-1] == ')':
            expression = expression[1:-1]
        parens = []
        start = 0
        # splits expression up into command and terms
        for i,c in enumerate(expression):
            if c == ' ':
                if len(parens) == 0:
                    cmds.append(expression[start:i])
                    start = i+1
            elif c == '(':
                parens.append(i)
            elif c == ')':
                start2 = parens.pop()
                if len(parens) == 0:
                    cmds.append(expression[start2+1 : i])
                start = i+1
        cmds.append(expression[start:])
        # removes empty terms
        cmds = [c for c in cmds if len(c) > 0]
        # print("break_expr output: ", cmds)
        return cmds

    def evaluate(self, expression, var={}):
        """
        :type expression: str
        :rtype: int
        """
        # print("evaluate was given: ", expression)
        expr = self.break_expr(expression)
        if expr[0] == "add":
            term1 = self.evaluate(expr[1], deepcopy(var))
            term2 = self.evaluate(expr[2], deepcopy(var))
            result = term1 + term2
        elif expr[0] == "mult":
            term1 = self.evaluate(expr[1], deepcopy(var))
            term2 = self.evaluate(expr[2], deepcopy(var))
            result = term1 * term2
        elif expr[0] == "let":
            for i in range(1, len(expr)-1, 2):
                var[expr[i]] = self.evaluate(expr[i+1], deepcopy(var))
            result = self.evaluate(expr[-1], deepcopy(var))
        else:
            if not (expr[0][0].isdigit() or expr[0][0] == '-'): # is variable
                result = var[expr[0]]
            else:
                result = int(expr[0])
        return result
