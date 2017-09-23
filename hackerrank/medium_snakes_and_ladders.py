# graph_snakes_and_ladders

def findBest(i, loc):
    if i == 100:
        return 0
    if i >= 95:
        return 1
    else:
        cand = []
        for j in range(1,7):
            best = findBest(loc[i+j], loc)
            print(best)
            if best[1] == 100:
                cand.push(best[0])
            if cand:
                return (min(cand)+1,100)
            else:
                return (-1,-1)

T = int(input())
for t in range(T):
    n_l = int(input())
    loc = [i for i in range(100)]
    for l in range(n_l):
        s, e = [int(i) for i in input().split()]
        loc[s] = e
    n_s = int(input())
    for s in range(n_s):
        st, en = [int(i) for i in input().split()]
        loc[st] = en
    curr = 1
    result = findBest(curr, loc)
    print(result)
        
        
