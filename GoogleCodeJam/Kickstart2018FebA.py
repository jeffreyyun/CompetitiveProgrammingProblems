def numBuses(buses, cities):
    result = []
    for c in cities:
        count = 0
        for s, e in buses:
            count += (s <= c <= e)
        result.append(count)
    return result

T = int(input())
for _ in range(T):
    N = int(input())
    x = [int(x) for x in input().split()]
    buses = [(x[i],x[i+1]) for i in range(0,N*2,2)]
    P = int(input())
    cities = []
    for i in range(P):
        cities.append(int(input()))

    result = numBuses(buses, cities)
    result = ' '.join(map(str, result))
    print("Case #{}: {}".format(_+1, result))
    __ = input()
