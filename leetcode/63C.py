class Solution(object):
    def countCornerRectangles(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        R = len(grid)
        C = len(grid[0])

        oneLocs = [[] for i in range(R)]

        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    oneLocs[r].append(c)

        ht = {}
        for r in range(R):
            L = len(oneLocs[r])
            for i in range(L):
                for j in range(i+1, L):
                    key = (oneLocs[r][i],oneLocs[r][j])
                    if key not in ht:
                        ht[key] = 0
                    ht[key] += 1

        total = 0
        for rowGroup in ht.keys():
            n = ht[rowGroup]
            total += (n*n - n)//2

        return total