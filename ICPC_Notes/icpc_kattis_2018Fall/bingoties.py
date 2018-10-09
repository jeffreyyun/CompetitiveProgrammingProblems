# A: Bingo Ties
# "9 for-loops"

def simulate(N, cards, first_row, second_row, first, second):
    # Try to tie the smallest cards
    # IMPLEMENT ME
    return first, second

def solve(N):
    cards = []
    locs = {}
    first, second = N+1, N+1
    for i in range(1, N+1):
        card = []
        for r in range(5):
            row = list(map(int, input().split()))
            card.append(row)
            for n in row:
                locs.setdefault(n, (i, r))  # TODO: account for (i, x) pairs
                if locs[n][0] != i:
                    if locs[n][0] < first:
                        first = locs[n][0]
                        first_row = cards[locs[n][1]]
                        second = i
                        second_row = row
                    elif locs[n][0] == first and i < second:
                        second = i
                        second_row = row
        if i != N:
            _ = input()
        cards.append(card)
    if first < N+1:
        # first, second = simulate(N, cards, first_row, second_row, first, second)
        result = "{} {}".format(first, second)
        return result
    return "no ties"


N = int(input())
result = solve(N)
print(result)

def generate(N):
    for i in range(N):
        for j in range(5):
            for k in range(5):
                print(i*25+j*5+k, end=" ")
            print()
        print()