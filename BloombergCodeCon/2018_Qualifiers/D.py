#Problem        : Passport Control
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

N = int(input())
M = int(input())

groups = []
for _ in range(M):
    groups.append(int(input()))

curr_left = [0 for _ in range(N)]
processed_groups = [0 for _ in range(N)]
total = [0 for _ in range(N)]

def addGroup(g):
    # add group to smallest available
    for i in range(N):
        if curr_left[i] == 0:
            curr_left[i] = g
            total[i] += 1
            processed_groups[i] += 1
            if processed_groups[i] == 10:
                curr_left[i] += 5
                processed_groups[i] = 0
            return

def process():

    addGroup(g)

    # advance time until available
    mg = min(curr_left)
    for i in range(N):
        curr_left[i] -= mg


# for each passenger group, advance time
for g in groups:
    process()
    
# assert(sum(total) == M)
print(' '.join(map(str, total)))