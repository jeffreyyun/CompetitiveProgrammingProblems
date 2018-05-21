#Problem        : 2016 Qualifiers - Lannisters of Justice
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys
import queue

data = sys.stdin.read().splitlines()

expr = data[0]


def eval(expr):

    precedence = {}
    # precedence['+'] = 1
    # precedence['-'] = 1
    # precedence['*'] = 2
    # precedence['/'] = 2
    precedence['+'] = 2
    precedence['-'] = 4
    precedence['*'] = 1
    precedence['/'] = 3

    def extractTokens(expr):
        curr = ""
        tokens = []
        for c in expr:
            if c in precedence:
                if curr != "":
                    tokens.append(curr)
                    curr = ""
                tokens.append(c)
            else:
                curr += c
        tokens.append(curr)
        return tokens

    # Infix to Postfix
    def ShuntingYard(tokens):
        output = []
        ops = []
        for t in tokens:
            if t in precedence: # operator
                while len(ops) > 0 and precedence[ops[-1]] >= precedence[t]:
                    output.append(ops.pop())
                ops.append(t)
            else:
                output.append(int(t))

        # add remaining ops
        ops.reverse()
        return output + ops

    def evalInfix(expr):
        ops = []
        nums = []

        for t in expr:
            if t in precedence:
                assert(len(nums) >= 2)
                b = nums.pop()
                a = nums.pop()
                if t == '+':
                    final = a+b
                elif t == '-':
                    final = a-b
                elif t == '*':
                    final = a*b
                elif t == '/':
                    final = a/b
                nums.append(final)
            else:
                nums.append(t)

        assert(len(nums) == 1)
        return int(nums[0])

    tokens = extractTokens(expr)
    infix = ShuntingYard(tokens)

    # print(expr, tokens, infix)
    result = evalInfix(infix)
    return result

print(eval(expr))