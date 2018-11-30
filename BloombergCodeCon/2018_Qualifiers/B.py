#Problem        : Bit Flip
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

S = list(input())
tmx = 0

# input small enough to do brute force
for i in range(32):
    temp = S[i]
    S[i] = '1'
    curr = 0
    mx = 0
    
    for c in S:
        if c == '1':
            curr += 1
        else:
            mx = max(curr, mx)
            curr = 0
    mx = max(curr, mx)
    S[i] = temp
    
    
    tmx = max(mx, tmx)
print(tmx)
