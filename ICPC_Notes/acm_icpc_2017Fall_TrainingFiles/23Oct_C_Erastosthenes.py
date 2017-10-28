import math

BIGNUM = 500005
primes = [True for i in range(BIGNUM)]

def setupPrime():

    primes[1] = False
    for n in [2]:
        for i in range(4, BIGNUM, 2):
            primes[i] = False
    for n in range(3, BIGNUM, 2):
        for i in range(n*2, BIGNUM, n):
            primes[i] = False


def sieve(a,b):
    ans = []
    for n in range(a,b+1):
        if primes[n]:
            ans.append(n)
    ans = ' '.join([str(i) for i in ans])
    print(ans)



setupPrime()

a,b = [int(i) for i in input().split()]
sieve(a,b)
