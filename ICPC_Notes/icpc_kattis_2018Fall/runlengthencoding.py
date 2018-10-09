def encode(S):
    """ Encode S as run-length decoding """
    curr = S[0]
    count = 1
    res = ""
    for c in S[1:]:
        if curr != c:
            res += curr + str(count)
            curr = c
            count = 1
        else:
            count += 1
    res += curr + str(count)
    return res

def decode(S):
    i = 0
    res = ""
    while i < len(S):
        curr = S[i]
        count = ""
        i += 1
        while i < len(S) and S[i].isnumeric():
            count += S[i]
            i += 1
        res += curr*int(count)
    return res

mode, S = input().split()
if mode == "E":
    res = encode(S)
else:
    res = decode(S)
print(res)