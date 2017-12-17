def ContiguousSequenceO(arr):
    max_sum = 0
    curr_sum = 0
    for i in range(len(arr)):
        curr_sum += arr[i]
        if curr_sum < 0:
            curr_sum = 0
        max_sum = max(curr_sum, max_sum)
    return max_sum


inp = [2,-1,2]
ret = ContiguousSequenceO(inp)
print(ret)
