def findIndOfSmaller(ltf, number):
    # binary search for [INDEX] of LARGEST number smaller than "number"
    # Input: ltf (list of ints), number (int)
    # Output: index
    left = 0
    right = len(ltf) - 1
    while left <= right:
        middle = left + (right-left)//2
        if ltf[middle] > number:
            right = middle - 1
        else:
            left = middle + 1
    return left

def createLTF(arr):
    # creates largest_thus_far list from given list
    ltf = [i for i in arr]
    if len(arr) == 0:
        return ltf
    curr_max = ltf[0]
    for i, num in enumerate(ltf):
        if num > curr_max:
            curr_max = num
        else:
            ltf[i] = curr_max
    return ltf

def subSort(arr):
    # Finds smallest subset to sort for entire list to be sorted
    # Returns the bounds
    """
    # Time: O(N log N) -- binary search for each element in list
    # Space: O(N)
    ltf = createLTF(arr)
    left_bound = max(len(arr)-1, 0)
    right_bound = 0
    # traverses array
    # note: don't do arr[1:] since enumerate would be off by 1
    for i,num in enumerate(arr):
        smaller_ind = findIndOfSmaller(ltf, num)
        if smaller_ind < i:
            right_bound = i
            left_bound = min(left_bound, smaller_ind)
    if right_bound <= left_bound:
        return (0, 0)
    else:
        return (left_bound, right_bound)
    """

    ### OPTIMAL SOLUTION
    # Time: O(N)
    # Space: O(1)

    def findLeftLNDS(arr):
        middle_start = 0
        for i in range(1, len(arr)):
            if arr[i] < arr[i-1]:
                middle_start = i
                return middle_start
        return 0

    def findRightLNDS(arr):
        middle_end = len(arr) - 1
        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > arr[i+1]:
                middle_end = i
                return middle_end
        return 0

    # get longest non-decreasing subsequence
    N = len(arr)
    middle_start = findLeftLNDS(arr)
    middle_end = findRightLNDS(arr)

    if middle_start != 0 or middle_end != 0:
        min_midright = min(arr[middle_start:])
        max_midleft = max(arr[:middle_end+1])

        # LIS next to each other
        if middle_start >= middle_end:
            middle_start, middle_end = middle_end, middle_start

        # shift bounds of to-be-sorted subset (middle)
        while middle_start-1 >= 0 and arr[middle_start-1] > min_midright:
            middle_start -= 1
        while middle_end+1 <= N-1 and arr[middle_end+1] < max_midleft:
            middle_end += 1

    return (middle_start, middle_end)


inp = [2,1]
ret = subSort(inp)
print(ret)
