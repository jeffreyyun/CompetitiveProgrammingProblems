class Solution(object):
    def containVirus(self, grid):
        """
        :type self.grid: List[List[int]]
        :rtype: int
        """
        def simulateTurn():
            # if none infected, return true... can print now
            printGrid(self.grid)
            print(self.wallCount)
            wallLocs = findBestRegion()
            self.wallCount += len(wallLocs)
            buildWalls(wallLocs)
            infected = infect()
            return (infected > 0)

        def findBestRegion():
            bestWalls = set()
            bestInfected = 0
            visited = [[False for _ in range(C)] for _ in range(R)]
            for i in range(R):
                for j in range(C):
                    if self.grid[i][j] and not visited[i][j]:
                        myWalls = set()
                        myInfected = set()
                        st = [(i, j)]
                        while len(st) > 0:
                            cx, cy = st.pop()
                            visited[cx][cy] = True
                            # check neighbors
                            for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                                if cx+dx >= 0 and cx+dx < R and cy+dy >= 0 and cy+dy < C:
                                    if self.grid[cx+dx][cy+dy] and not visited[cx+dx][cy+dy]:
                                        st.append((cx+dx, cy+dy))
                                    elif self.grid[cx+dx][cy+dy] == 0:
                                        if (cx,cy,cx+dx,cy+dy) not in walls:
                                            myInfected.add((cx+dx,cy+dy))
                                            myWalls.add((cx,cy,cx+dx,cy+dy))

                        if len(myInfected) > bestInfected:
                            bestInfected = len(myInfected)
                            bestWalls = myWalls
                        print(myInfected, len(myWalls))
            return bestWalls


        def buildWalls(wallLocs):
            for wall in wallLocs:
                walls.add(wall)

        def printGrid(grid):
            print()
            for r in grid:
                print(''.join([str(i) for i in r]))

        def infect():
            infected = 0
            visited = [[False for _ in range(C)] for _ in range(R)]
            nextGrid = [[_ for _ in r] for r in self.grid]
            for i in range(R):
                for j in range(C):
                    if self.grid[i][j] and not visited[i][j]:
                        st = [(i, j)]
                        while len(st) > 0:
                            cx, cy = st.pop()
                            visited[cx][cy] = True
                            # check neighbors
                            for dx, dy in [(-1,0),(1,0),(0,1),(0,-1)]:
                                if cx+dx >= 0 and cx+dx < R and cy+dy >= 0 and cy+dy < C:
                                    if self.grid[cx+dx][cy+dy] and not visited[cx+dx][cy+dy]:
                                        st.append((cx+dx, cy+dy))
                                    elif nextGrid[cx+dx][cy+dy] == 0:
                                        if (cx,cy,cx+dx,cy+dy) not in walls:
                                            infected += 1
                                            nextGrid[cx+dx][cy+dy] = 1
            self.grid = nextGrid
            return infected

        self.grid = grid
        R = len(self.grid)
        C = len(self.grid[0])
        walls = set()

        self.wallCount = 0
        while simulateTurn():
            pass

        return self.wallCount


sol = Solution()

grid = [[0,0,1,1,1,0,1,0,0,0],[1,1,1,0,0,0,1,1,0,1],[0,0,0,0,0,0,1,0,0,0],[0,0,0,0,1,0,1,0,0,0],[1,0,0,0,1,1,1,0,0,0],[0,0,0,1,0,1,1,0,0,0],[1,0,0,0,0,1,0,0,0,1],[1,0,0,0,0,0,0,0,0,1],[0,1,0,0,0,0,0,0,1,0],[1,1,0,0,0,1,0,1,0,0]]
# TODO: Fix above example
# Expected: 59, Gives: 68
ppp = sol.containVirus(grid)
print(ppp)
