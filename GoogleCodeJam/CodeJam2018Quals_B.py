"""
O(N log N)
"""

def solve():
    N = int(input())
    nums = list(map(int, input().split()))
    # N = len(nums)
    evens = nums[::2]
    odds = nums[1::2]
    evens.sort()
    odds.sort()
    nums[::2] = evens
    nums[1::2] = odds
    for i in range(N//2):
        if odds[i] < evens[i]:
            return 2*i
    return "OK"


T = int(input())
for _ in range(T):
    ans = solve()
    print("Case #{}: {}".format(_+1, ans))
