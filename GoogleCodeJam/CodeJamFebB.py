import sys
import queue


# Time: O(L)
# Space: O(L)
def CEOSearch(L, emp):

    # emp -- {experience: (# employees, # management slots)}
    result = 0
    levels = sorted(emp.keys())

    # PQ of exp levels and management slots
    pq = queue.PriorityQueue()
    for l in levels:
        pq.put((l, emp[l]*l))

    # For each employee, assign a direct manager
    # In other words, decrement management slots of people above them
    for l in levels:
        # CEO must direct manage all remaining employees
        if pq.empty():
            result += emp[l]
            continue

        while emp[l] > 0:
            exp = 0
            # Find higher experience managers
            if not pq.empty():
                exp, slots = pq.get()
                # print("First", exp, slots)
            while exp <= l and not pq.empty():
                exp, slots = pq.get()
                # print("While", exp, slots)

            if exp <= l and pq.empty():
                result += emp[l]
                emp[l] = 0
            else:
                # more employees than slots
                if emp[l] > slots:
                    emp[l] -= slots
                # more slots than employees -- add these slots back
                else:
                    pq.put((exp, slots - emp[l]))
                    emp[l] = 0

            # print("Level {}, num{} --> level{} slots{}".format(l, emp[l],exp,slots))


    result = max(result, levels[-1]+1)
    return result


sys.stdin = open("B-large-practice.in", "r")
sys.stdout = open("B-large.out", "w")

T = int(input())
for t in range(T):
    L = int(input())
    employees = {}
    for i in range(L):
        num, exp = map(int, input().split())
        employees[exp] = num
    print("Case #{}: {}".format(t+1, CEOSearch(L, employees)))

