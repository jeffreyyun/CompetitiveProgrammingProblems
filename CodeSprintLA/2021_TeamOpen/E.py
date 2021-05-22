import functools

def minOperationsUtil(arr):
    @functools.lru_cache(None)
    def minOperations(i, j):
        # Base Case
        if i >= N or j >= N:
            return 0
        #
        if arrSorted[i] < arr[j]:
            return 1 + minOperations(i + 1, j + 1)
        # Move to end / move to start (sim by advancing one index)
        return max(minOperations(i, j + 1), minOperations(i + 1, j))

    arrSorted = sorted(arr)
    if arr == arrSorted:
        return 0
    return minOperations(0, 0)

N = int(input())
arr = list(map(int, input().split()))
ans = minOperationsUtil(arr)
print(ans)