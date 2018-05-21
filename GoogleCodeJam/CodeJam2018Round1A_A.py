def solve():
    R, C, H, V = map(int, input().split())
    chips = [[0 for _ in range(C)] for __ in range(R)]
    hcuts = [0 for _ in range(H)]
    vcuts = [0 for _ in range(V)]
    # Read in the array of choco-chips and build cumulative chips array
    for i in range(R):
        row = input()
        row_chips = 0
        for j in range(C):
            row_chips += (row[j] == '@')
            chips[i][j] = chips[i-1][j] + row_chips if i != 0 else row_chips
    total_chips = chips[-1][-1]
    horiz_chips = total_chips/(H+1)
    vert_chips = total_chips/(V+1)
    piece_chips = total_chips/((H+1)*(V+1))

    # determine indices of horizontal cuts
    curr = 0
    for i in range(H):
        while chips[curr][-1] < (i+1)*horiz_chips:
            curr += 1
            if curr >= R or chips[curr][-1] > (i+1)*horiz_chips:
                return "IMPOSSIBLE"
        hcuts[i] = curr
    hcuts.append(-1)

    # determine indices of vertical cuts
    curr = 0
    for i in range(V):
        while chips[-1][curr] < (i+1)*vert_chips:
            curr += 1
            if curr >= C or chips[-1][curr] > (i+1)*vert_chips:
                return "IMPOSSIBLE"
        vcuts[i] = curr
    vcuts.append(-1)

    # check if the cuts work
    for a in range(H+1):
        for b in range(V+1):
            if chips[hcuts[a]][vcuts[b]] != (a+1)*(b+1)*piece_chips:
                return "IMPOSSIBLE"
    return "POSSIBLE"


T = int(input())
for t in range(T):
    ans = solve()
    print("Case #{}: {}".format(t+1, ans))
