class Solution:
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        # Goal: Find longest shortest path
        # Need to find shortest distance from K to each node...
        # Setup Graph
        # g = [{} for i in range(N)]
        # for edge in times:
        #     u, v, w = edge
        #     if v not in g[u]:
        #         g[u][v] = w
        #     else:
        #         g[u][v] = min(g[u][v], w)

        # Bellman-Ford algorithm!!!

        INF = 9999999999
        N += 1
        distance = [INF]*N
        distance[0] = -1
        distance[K] = 0

        for _ in range(N):
            for edge in times:
                u, v, w = edge
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

        res = max(distance)
        return res if res != INF else -1