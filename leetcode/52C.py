#!/bin/python3


class Solution:
    def buildGrid(self):
        N = self.N
        grid = [[1 for i in range(N+4)] for i in range(N+4)]
        for row in [0, 1, N+2, N+3]:
            grid[row] = [0 for i in range(N+4)]
        for i in range(N+4):
            grid[i][0] = 0
            grid[i][1] = 0
            grid[i][N+2] = 0
            grid[i][N+3] = 0
        self.grid = grid
        return

    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        self.N = N
        self.buildGrid()
        count = 0
        while (count < K):
            count += 1
            self.turn()
        return self.grid[r+2][c+2]/(pow(8, K))

    def turn(self):
        N = self.N
        grid = self.grid
        copy = [[grid[i][j] for j in range(N+4)] for i in range(N+4)]
        dr = [-2, -2, -1, -1, 1, 1, 2, 2]
        dc = [1, -1, 2, -2, 2, -2, 1, -1]
        for r in range(2, N+2):
            for c in range(2, N+2):
                copy[r][c] = 0
                for i in range(8):
                    copy[r][c] += grid[r + dr[i]][c + dc[i]]
        self.grid = copy
        return


sol = Solution()

ppp = sol.knightProbability(3, 2, 0, 0)
print(ppp)