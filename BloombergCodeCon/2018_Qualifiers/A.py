#Problem        : A Very Odd Problem
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

N = int(input())
nums = list(map(int, input().split()))
ct = 0
for n in nums:
    ct += (n % 2 == 0)
ans = "YES" if ct >= 2 else "NO"
print(ans)