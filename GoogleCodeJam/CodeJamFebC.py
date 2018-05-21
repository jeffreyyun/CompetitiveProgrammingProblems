import sys
import itertools

# Time: O(L)
# Space: O(L)
def centrist(L, N):
    diffs = None
    result = [None, None, None]

    # STEP 1: Get diffs (O(L))
    # print(N)
    for i in range(L):
        if not diffs:
            if not (N[0][i] == N[1][i] == N[2][i]):
                diffs = [N[x][i] for x in range(3)]
                # first letters are different
                if len(set(diffs)) == 3:
                    return "YES YES YES"
                else:
                    # Find the certain NO
                    for x in range(3):
                        if diffs.count(diffs[x]) == 1:
                            result[x] = "NO"
                            firstDiffLetter = diffs[x]
                            secondDiffLetter = diffs[x-1]
        else:
            cand = [diffs[x]+N[x][i] for x in range(3)]
            if len(set(cand)) == 3:
                diffs = cand
                break

    # print("diffs are", diffs)
    
    # STEP 2: Evaluate the 6 possible perms for this diffs (O(1))
    # Check each perm to see if the ordering is possible
    for perm in itertools.permutations(diffs):
        middle = diffs.index(perm[1])
        # print("result listing, perm[1]: {}, result:{}".format(perm[1], result[middle]))
        if result[middle] == "NO":
            continue

        valid = True
        # if firstDiffLetter at beginning, firstDiffLetter < secondDiffLetter
        if perm[0][0] == firstDiffLetter:
            if perm[1][1] == secondDiffLetter and perm[2][1] == firstDiffLetter:
                valid = False
        else: # secondDiffLetter at beginning
            if perm[0][1] == firstDiffLetter and perm[1][1] == secondDiffLetter:
                valid = False

        if valid:
            # If no inconsistency in ordering rules e.g. AB CC BA, BA CC AB
            # print("valid perm is", perm)
            result[middle] = "YES"

    for i in range(3):
        result[i] = "NO" if not result[i] else result[i]

    return ' '.join(result)



def naive(L, N):
    # TIme: O(L!)
    ans = ["NO"]*3
    for pos in itertools.permutations('ABC'):
        ref = sorted(N, key=lambda x: [pos.index(c) for c in x])
        for i in range(3):
            if ref[1] == N[i]:
                ans[i] = "YES"
    return ' '.join(ans)


sys.stdin = open("C-large-practice.in", "r")
sys.stdout = open("C-large.out", "w")

T = int(input())
for t in range(T):
    L = int(input())
    N = [x for x in input().split()]
    print("Case #{}: {}".format(t+1, centrist(L, N)))