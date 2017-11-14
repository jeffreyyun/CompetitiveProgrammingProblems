def getPositiveSeq(arr, i):
    positive_seq = 0
    while i < len(arr) and arr[i] >= 0:
        positive_seq += arr[i]
        i += 1
    return positive_seq, i

def getNegativeSeq(arr, i):
    negative_seq = 0
    while i < len(arr) and arr[i] <= 0:
        negative_seq += arr[i]
        i += 1
    return negative_seq, i

def ContiguousSequence(arr):
    # finds contiguous sequence with largest sum
    N = len(arr)
    if N <= 0:
        return 0

    max_sum = max(arr)      # all negative
    if max_sum < 0:
        return max_sum

    i = 0
    _, i = getNegativeSeq(arr, i)

    positive_seq, i = getPositiveSeq(arr, i)
    max_sum = max(max_sum, positive_seq)

    # loops to obtain the positive seqs
    while i < N:
        # resets
        running_sum = positive_seq

        while i < N and running_sum > 0:
            # adds next negative and positive
            negative_seq, i = getNegativeSeq(arr, i)
            running_sum += negative_seq
            positive_seq, i = getPositiveSeq(arr, i)
            running_sum += positive_seq

            # updates max_sum
            max_sum = max(max_sum, running_sum)

    return max_sum


### the optimal solution....... wow
def ContiguousSequenceO(arr):
    max_sum = 0
    running_sum = 0
    for i in range(len(arr)):
        running_sum += arr[i]
        if running_sum < 0:
            running_sum = 0
        max_sum = max(running_sum, max_sum)
    return max_sum


inp = [2,-1,2]
ret = ContiguousSequenceO(inp)
print(ret)
