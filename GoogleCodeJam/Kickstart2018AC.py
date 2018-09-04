def solve(words, S1, S2, N, A, B, C, D):
    """
    Time: O(M + N * sqrt(M))
    Space: O(L)
    """
    # generate S
    x = [0 for i in range(N)]
    x[0], x[1] = ord(S1), ord(S2)
    for i in range(2, N):
        x[i] = (A * x[i - 1] + B * x[i - 2] + C) % D
    S = S1 + S2 + ''.join([chr(97 + x[i] % 26) for i in range(2, N)])

    # chunk words by (first, last, freq table)
    temp = words
    words = dict()
    word_lengths = set()
    for w in temp:  # O(M), where M = total words length
        ht = [0]*26
        for c in w:
            ht[ord(c)-97] += 1
        key = (w[0], w[-1], tuple(ht))
        words.setdefault(key, 0)
        words[key] += 1
        word_lengths.add(len(w))

    count = 0
    for k in word_lengths: # O(# distinct word lengths) = O(sqrt(M))
        # Keep track of freq in S
        htS = [0] * 26
        for c in S[:k]:
            htS[ord(c) - 97] += 1
        key = (S[0], S[k-1], tuple(htS))
        if key in words:
            count += words[key]
            del words[key]
        # Iterate through S
        for i in range(k, N):  # O(N)
            htS[ord(S[i])-97] += 1
            htS[ord(S[i - k]) - 97] -= 1
            key = (S[i-k+1], S[i], tuple(htS))
            # print("{} {}\n{} {}\n\n".format(S[i-k+1:i+1], htS, w, ht))
            if key in words:
                count += words[key]
                del words[key]
    return count


T = int(input())
for t in range(T):
    L = int(input())
    words = input().split()
    S1, S2, N, A, B, C, D = input().split()
    N, A, B, C, D = map(int, [N,A,B,C,D])
    print("Case #{}: {}".format(t+1, solve(words,S1,S2,N,A,B,C,D)))
