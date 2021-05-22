import random, math, sys

TEST = False
VERBOSE = False

def updateInterval(curr, guess, res):
    left, right = curr
    if res == 'yes': # [10,20] [15,25]
        left = max(curr[0], guess[0])
        right = min(curr[1], guess[1])
    else:
        # if guess interval is right of curr, shrink right
        if guess[0] > curr[0]:
            right = min(curr[1], guess[0]-1)
        elif guess[1] < curr[1]:    # shrink left
            left = max(curr[0], guess[1]+1)
        else:
            if VERBOSE: print('fail!')
    if VERBOSE: print(f'curr {curr} will be [{left} {right}]')
    return [left, right]

def getGuess(steve, alex):
    # IF intervals non-overlapping, put your bounds in middle of intervals to eliminate
    if alex[0] > steve[1] or steve[0] > alex[1]:
        steveMid = math.floor(sum(steve)/2)
        alexMid = math.floor(sum(alex)/2)

        # if steveMid is length 2
        if steve[1]-steve[0]==1:
            if steve[1] < alex[0]: steveMid = steve[1] # left
            else: steveMid = steve[0] # right

        if alex[1]-alex[0]==1:
            if alex[1] < steve[0]: alexMid = alex[1] # left
            else: alexMid = alex[0] # right

        return sorted([steveMid, alexMid])

    # if they're the same, just take the left half!
    return [steve[0], math.floor(sum(steve)/2)]


sn, an = random.randint(1,500), random.randint(1,500)
# sn,an = 250,251
if TEST or VERBOSE: print(f"Steve: {sn}, Alex: {an}")

def answerAsk(l, r):
    sa = "yes" if l <= sn <= r else "no"
    aa = "yes" if l <= an <= r else "no"
    if VERBOSE: print(f"{sa} {aa}")
    return sa, aa

def solve():
    steve = [1,500]
    alex = [1,500]
    for _ in range(10):
        guess = getGuess(steve, alex)
        guessLeft, guessRight = guess
        print(f"ASK {guessLeft} {guessRight}")
        sys.stdout.flush()

        if TEST:
            s, a = answerAsk(guessLeft, guessRight)
        else:
            s, a = input().split()
        steve = updateInterval(steve, guess, s)
        alex = updateInterval(alex, guess, a)
        if VERBOSE: print(f"Steve: {steve}, Alex: {alex}")
        if (steve[0] == steve[1] and alex[0] == alex[1]):
            print(f"GUESS {steve[0]} {alex[0]}")
            sys.stdout.flush()
            break
    if TEST or VERBOSE: print(f"YOU DONE steve: {steve}, alex: {alex}")

solve()
