#Problem        : BAssembly
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import sys

data = sys.stdin.read().splitlines()

N = int(data[0])
data = [l.split() for l in data]

stack = {}
for i in range(8):
    stack[chr(i + ord('a'))] = 0    # initialize regs

ans = None

def eval(b):
    if b in stack:
        return stack[b]
    else:
        return int(b)

i = 1
while i <= N:
    # print(data[i], stack)
    command = data[i][0]
    if len(data[i]) == 3:
        a, b = data[i][1], data[i][2]
    if command == "jmp":
        offset = data[i][1]
        offset = eval(offset)
        if offset == 0:
            offset = 1
        i += offset-1
    elif command == "ret":
        a = data[i][1]
        ans = eval(a)
        break
    elif command == "set":
        stack[a] = eval(b)
    elif command == 'add':
        stack[a] += eval(b)
    elif command == 'sub':
        stack[a] -= eval(b)
    elif command == 'mul':
        stack[a] *= eval(b)
    elif command == 'mod':
        stack[a] %= eval(b)
    else:
        stack[a] /= eval(b)
        stack[a] = int(stack[a])
    i += 1


print(ans)