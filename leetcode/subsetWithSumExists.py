def subsetWithSumExists(a, target):

    # if memo[i][j], then you can use a[0...i-1] to make sum of j
    memo = [[0 for i in range(target+1)] for j in range(len(a)+1)]

    for i in range(target+1):   # empty set
        memo[0][i] = 0
    for i in range(len(a)+1):     # sum of 0 can be made with any set
        memo[i][0] = 1

    for i in range(1, len(a)+1):
        for j in range(1, target+1):
            if j < a[i-1]:
                memo[i][j] = memo[i-1][j]
            else:
                memo[i][j] = memo[i-1][j] or memo[i-1][j-a[i-1]]

    printGrid(memo)

    return memo[len(a)][target]

def printGrid(grid):
    for r in grid:
        print(' '.join([str(x) for x in r]))


print(subsetWithSumExists([3,2,4,1], 6))