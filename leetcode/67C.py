class Solution:
    def orderOfLargestPlusSign(self, N, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        memo = [[[0, 0] for i in range(N)] for j in range(N)]
        grid = self.generateMines(N, mines)
        # self.prettyPrint(grid)

        # Get all widths
        for r in range(N):
            start = -1
            end = 0
            while end < N:
                if grid[r][end]:
                    end += 1
                else:
                    # 1's between start and end
                    for i in range(start+1, end):
                        memo[r][i][0] = min(end-i, i-start)
                    start = end
                    end += 1
            for i in range(start+1, end):
                memo[r][i][0] = min(end-i, i-start)

        # Get all heights
        for c in range(N):
            start = -1
            end = 0
            while end < N:
                if grid[end][c]:
                    end += 1
                else:
                    # 1's between start and end
                    for i in range(start+1, end):
                        memo[i][c][1] = min(end-i, i-start)
                    start = end
                    end += 1
            for i in range(start+1, end):
                memo[i][c][1] = min(end-i, i-start)


        best = 0
        for i in range(N):
            for j in range(N):
                best = max(best, min(memo[i][j]))

        return best

    def generateMines(self, N, mines):
        grid = [[1 for i in range(N)] for j in range(N)]
        for x, y in mines:
            grid[x][y] = 0
        return grid

    def prettyPrint(self, grid):
        for r in grid:
            print(r)


sol = Solution()
N=5
mines = [[4,2]]
# for i in range(100):
#     mines.append([random.randint(0,N-1), random.randint(0,N-1)])
# print(mines)

res = sol.orderOfLargestPlusSign(N, mines)
print(res)