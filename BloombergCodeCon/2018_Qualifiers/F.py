#Problem        : Ergonomics
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

# Calculate proximity of all 'O' --> assign most frequently appearing to them
R, C = map(int, input().split())
keyboard = []
for _ in range(R):
    keyboard.append(input())
S = input()

ht = {}
for c in S:
    if not c.isalpha():
        continue
    ht.setdefault(c, 0)
    ht[c] += 1
freqs = sorted(ht.values(), key = lambda x: -x)
    
# find dists of each key
Hkeys = []
dists = []
for i in range(R):
    for j in range(C):
        if keyboard[i][j] == 'H':
            Hkeys.append((i, j))
            dists.append(0)
for i in range(R):
    for j in range(C):
        if keyboard[i][j] == 'O':
            best_dist = 1000
            for hi, hj in Hkeys:
                best_dist = min(best_dist, abs(hi-i)+abs(hj-j))
            dists.append(best_dist)

# assign shortest dists to most frequent keys        
dists.sort()
i = 0
total = 0
while i < len(freqs):
    total += freqs[i]*dists[i]
    i += 1
print(total)
