class Solution:
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # https://discuss.leetcode.com/topic/113762/step-by-step-guidance-of-the-o-n-3-time-and-o-n-2-space-solution/2
        """
        DP -- (i, j)

        OPTIMAL SUBSTRUCTURE
        Score dependent on smaller problems (neighbor cells)

        OVERLAPPING SUBPROBLEMS
        Two ways to arrive in (i, j), two ways to leave (p, q)
        To ensure two ways don't overlap, we must have N = i+j = p+q

        Recurrence relation
        T(n, i, p) = grid[i][n-i] += max{T(n-1, i-1, p-1), T(n-1, i-1, p), T(n-1, i, p-1), T(n-1, i, p)}
        T(n, i, p) += grid[p][n-p] if i != p else 0

        Can have 2-D matrix since we only depend on one dimension (n-1)

        Time O(N^3), Space: O(N^2)
        """


        # maxSteps from (0, 0) => (N-1, N-1)
        N = len(grid)       # grid given as square
        maxSteps = 2*(N-1)

        dp = [[-1 for i in range(N)] for _ in range(N)]

        # Base Case
        dp[0][0] = grid[0][0]

        # Subproblems -- N steps to destination, N steps back
        for n in range(1, maxSteps+1):
            # We will overwrite dp from Bottom Right to Top Left as we go
            for i in range(N)[::-1]:
                for p in range(N)[::-1]:
                    j = n-i
                    q = n-p

                    # valid movement to/from
                    if j<0 or j>=N or q<0 or q>=N or grid[i][j]==-1 or grid[p][q]==-1:
                        # dp[i][p] = -1
                        continue

                    # Take maximum of possible paths to/from
                    if i > 0:
                        dp[i][p] = max(dp[i][p], dp[i-1][p])
                    if p > 0:
                        dp[i][p] = max(dp[i][p], dp[i][p-1])
                    if i > 0 and p > 0:
                        dp[i][p] = max(dp[i][p], dp[i-1][p-1])

                    if dp[i][p] != -1:
                        dp[i][p] += grid[i][j] + (grid[p][q] if i != p else 0)
            # print(dp)

        return max(dp[N-1][N-1], 0)     # 0 if no reachable path


sol = Solution()

grid =[[0, 1, -1], [1, 0, -1], [1, 1,  1]]

res = sol.cherryPickup(grid)
print(res)
