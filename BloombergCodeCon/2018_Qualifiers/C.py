#lexicographically smallest value, then smallest row, and then smallest column value.
R, C, K = map(int, input().split())
grid = []
for _ in range(R):
    grid.append(input().split())

# start is 0, 0
cx, cy = 0, 0 
path = grid[cx][cy]

for _ in range(K):
    # check neighboring tiles
    d = [(-1, 0), (0, -1), (0, 1), (1, 0)]        # smallest row, smallest col
    bx, by = None, None
    for dx, dy in d:
        nx, ny = cx+dx, cy+dy
        if 0 <= nx < R and 0 <= ny < C and grid[nx][ny] != grid[cx][cy]:
            if bx == None:
                bx, by = nx, ny
            elif grid[nx][ny] < grid[bx][by]:
                bx, by = nx, ny
    cx, cy = bx, by
    path += grid[cx][cy]
    
print(path)