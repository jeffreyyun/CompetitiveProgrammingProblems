class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = 0
        rows = len(grid)
        if not rows:
            return 0
        cols = len(grid[0])
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        for r in range(rows):
            for c in range(cols):
                # DFS
                if grid[r][c] == 1:
                    q = [(r,c)]
                    grid[r][c]=0
                    curr = 0
                    while len(q)>0:
                        r, c = q.pop()
                        curr += 1
                        for d in dirs:
                            if check(r+d[0],c+d[1], grid):
                                q.append((r+d[0],c+d[1]))
                    m = max(m, curr)
        return m


def check(r, c, grid):
    rows = len(grid)
    cols = len(grid[0])
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return False
    if grid[r][c]==1:
        grid[r][c]=0
        return True
    else:
        return False


# breadth first search

sol = Solution()

inp = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

ppp = sol.maxAreaOfIsland(inp)

print(ppp)