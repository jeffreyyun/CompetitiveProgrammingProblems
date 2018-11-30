#Problem        : Candy Thief
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

import copy

C, N = map(int, input().split())
rows = []
possible = set()
for _ in range(N):
    line = input().split()
    curr = int(line[0])
    people = line[1:]
    rows.append([curr, set(people)])
    for p in people:
        possible.add(p)
all_people = copy.copy(possible)

# Find all people present when candies are stolen
for i in range(0, N):
    prev_candies = rows[i-1][0] if i != 0 else C
    if rows[i][0] < prev_candies:   # if candy stolen
        for p in list(possible):  
            if p not in rows[i][1]:   # if p not present
                possible.remove(p)

possible_kids = copy.copy(possible)
ans = []
possible_parents = copy.copy(all_people)

# For each of those people,
for k in possible_kids:
    possible = copy.copy(possible_parents)
    possible.remove(k)
    not_steal_time = False
    # for each time candies are not stolen,
    # find all possible parents --> does anyone appear at all of those times?
    for i in range(N):
        if k not in rows[i][1]:   # kid not present either
            # for p in list(possible):
            #     if p in rows[i][1]:
            #         possible.remove(p)
            continue
        prev_candies = rows[i-1][0] if i != 0 else C
        if rows[i][0] == prev_candies:  # if candy not stolen, why?
            not_steal_time = True
            for p in list(possible):          # you can't be the parent
                if p not in rows[i][1]:
                    possible.remove(p)
        if rows[i][0] < prev_candies:
            for p in list(possible):
                if p in rows[i][1]:
                    possible.remove(p)
    if len(possible) == 1:
        # if never shows up with kid, we don't know!
        for p in possible:
            together = False
            for i in range(N):
                if k in rows[i][1] and p in rows[i][1]:
                    together = True
            if together:
                ans.append([k, p])
            else:
                ans.append([k, "UNKNOWN"])
    elif len(possible) == 0 and not_steal_time:
        # no parents and you still don't steal? not the kid!
        pass
    else:
        ans.append([k, "UNKNOWN"])
    # print("kid: {}, possible_parents: {}".format(k, possible))
        
# print("possible_kids: {}".format(possible_kids))

# if multiple pairs, print UNKNOWN
if len(ans) >= 2:
    print("UNKNOWN")
else:
    print("{} {}".format(ans[0][0], ans[0][1]))