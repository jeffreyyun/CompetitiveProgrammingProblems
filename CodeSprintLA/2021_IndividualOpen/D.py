
# find subset sum divisble by N
def findSubsetDivisibleByN(N, candies):
    NC = len(candies)
    def help(ind=0, total=0, path=[]):
        for i in range(ind+1, NC):
            if (total+candies[i]) % N == 0: # base case
                return path+[i+1]
            tmp = help(i, total+candies[i], path+[i+1])
            if tmp: return tmp  # if it works, great!!

    tmp = help(-1, 0, [])
    return tmp

N = int(input())
candies = list(map(int, input().split()))
ans = findSubsetDivisibleByN(N, NC, candies)
if not ans:
    print(-1)
else:
    print(len(ans))
    print(' '.join(map(str, ans)))
