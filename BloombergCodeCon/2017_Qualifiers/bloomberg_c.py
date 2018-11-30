#Problem        : Dependency Gambit
#Language       : Python 3
#Compiled Using : py_compile
#Version        : Python 3.4.3
#Input for your program will be provided from STDIN
#Print out all output from your program to STDOUT

# DFS -- O(N+D), N- libs, D-pairs of dependencies

def doDFS(lib):
    if lib in orders:
        return orders[lib]
    order = 0
    # find order for each dependency
    for d in deps[lib]:
        order = max(order, doDFS(d)+1)
    # set order for this lib
    turns[order].append(lib)
    orders[lib] = order
    return order

# get inputs
target = input()
N = int(input())
deps = {}
orders = {}
turns = [[] for i in range(99999)]

libs = set()

# set up graph
for i in range(N):
    L = input().split()
    lib_name = L[0]
    my_deps = L[2:]
    deps[lib_name] = my_deps

    libs.add(lib_name)

# find order of target -- doDFS recurses
target_order = doDFS(target)
orders[target] = target_order
turns[target_order] = [target]

ans = []
for t in turns:
    ans += sorted(t)

print(' '.join(ans))