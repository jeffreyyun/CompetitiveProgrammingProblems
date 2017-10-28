import math


def isPrime(n):
    if n % 2 == 0 or n == 1:
        if n == 2:
            return True
        return False
    BIGNUM = int(math.sqrt(n))
    for i in range(3, BIGNUM+1, 2):
        if n % i == 0:
            return False
    return True



TC = int(input())
for _ in range(TC):
    n = int(input())
    if isPrime(n):
        print("Prime")
    else:
        print("Not prime")
