class Solution(object):
    def numDistinctIslands(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        dirs = [(0,1),(-1,0),(0,-1),(1,0)] # NESW
        shapes = []
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    m_shape=[]
                    q = [(r,c,0,0)]
                    grid[r][c]=0
                    # store sequence of distances (DFS used here) from the first 1
                    while len(q)>0:
                        mr,mc,dx,dy = q.pop()
                        for d in dirs:
                            if check(mr+d[0],mc+d[1], grid):
                                q.append((mr+d[0],mc+d[1],dx+d[0],dy+d[1]))
                                m_shape.append((dx+d[0],dy+d[1]))
                    if m_shape not in shapes:
                        shapes.append(m_shape)
        return len(shapes)


def check(r, c, grid):
    rows = len(grid)
    cols = len(grid[0])
    if r < 0 or r >= rows or c < 0 or c >= cols:
        return False
    elif grid[r][c]==1:
        grid[r][c]=0
        return True
    else:
        return False


sol = Solution()

inp = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]

ppp = sol.numDistinctIslands(inp)

print(ppp)