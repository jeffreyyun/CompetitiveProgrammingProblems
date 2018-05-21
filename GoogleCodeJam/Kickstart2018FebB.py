import math

def getNum(k):
    base = "001001100011011"
    reverse = False
    # Divide and Conquer, essentially
    # "Pivot" 0's are always (power of 2)-th characters
    while k > 15:
        # print(k)
        reverse = not reverse
        pow2 = 1 << int(math.log2(k)//1)
        if k == pow2:
            return 0
        k = pow2 - (k - pow2)
    return (reverse ^ int(base[k-1]))

T = int(input())
for t in range(T):
    res = getNum(int(input()))
    print("Case #{}: {}".format(t+1, res))
