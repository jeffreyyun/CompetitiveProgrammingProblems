T = int(input())
for t in range(T):
    N = int(input())
    graph = {}
    notStart = set()
    sources = set()
    itinerary = []
    for i in range(N):
        source = input()
        dest = input()
        graph[source] = dest
        graph.setdefault(dest, None)
        notStart.add(dest)
        sources.add(source)
    for s in graph.keys():
        if s not in notStart:
            start = s
        elif s not in sources:
            end = s
    while start in sources:
        itinerary.append("{}-{}".format(start, graph[start]))
        start = graph[start]
    result = ' '.join(itinerary)
    print("Case #{}: {}".format(t+1, result))
