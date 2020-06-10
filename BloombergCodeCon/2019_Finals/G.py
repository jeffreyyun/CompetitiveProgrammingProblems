#Problem        : Crowded Party
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

# For intervals, how many guests will be there

# When we remove a guest we update the intervals    O(24)

def isLonely(g):    # for each guest, check if lonely -- O(24)*O(1000)
    b, e, f = g
    for t in range(b, e+1):
        if peeps[t]-1 < f:
            return True
    return False


N = int(input())
guests = [] # update this list every turn
peeps = [0 for _ in range(25)]
for _ in range(N):
    b, e, f = map(int, input().split())
    guests.append((b,e,f))
    for t in range(b, e+1):
        peeps[t] += 1

# filter out the lonely ones
lonely = True
while lonely and len(guests) > 0:
    lonely = False
    newguests = []
    for g in guests:
        if not isLonely(g):
            newguests.append(g)
        else:
            b, e, f = g
            for t in range(b, e+1):
                peeps[t] -= 1
            lonely = True
    guests = newguests
    
print(len(guests))
