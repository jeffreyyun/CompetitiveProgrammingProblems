def solve(N, S):
    N = len(S)+1
    i = 0
    count = 1
    res = []
    while i < N-1:
        if S[i] == 'R':
            res.append(count)
            count += 1
            i += 1
        elif S[i] == 'L':
            prevCount = count
            while i < N-1 and S[i] == 'L':  # count num of L
                count += 1
                i += 1
            res += list(range(count, prevCount-1, -1))    # R is the smallest num
            count += 1
            i += 1
    if S[-1] == 'R':
        res.append(count)
    return res


N = int(input())
S = input()
res = solve(N, S)
print('\n'.join(list(map(str, res))))
