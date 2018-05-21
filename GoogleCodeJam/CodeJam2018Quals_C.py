import sys

# Algorithm is not good --> see solution for simpler + better alg

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

def solve():
    A = int(input())
    grid = [[False for i in range(1000)] for j in range(1000)]
    borders = set()         # contains filled border cells for current round
    print(100,100)
    sys.stdout.flush()
    # Make a A == 20 area in the center..... keep on picking filled squares adjacent to boundary
    while True:
        x, y = map(int, input().split())
        if x == 0 and y == 0:
            return True
        elif x <= 0 or y <= 0:
            return False
        else:
            grid[x][y] = True
            borders.add((x, y))
        # pick square with unfilled squares averaging most filled neighbors
        dx = [-1,0,1,-1,0,1,-1,0,1]
        dy = [1,1,1,-1,-1,-1,0,0,0]
        bx, by = None, None
        average = 0

        # for each filled square and their unfilled neighbors,
        # average filled neighbors of their unfilled neighbors --> if high average, this is best
        for x, y in list(borders):
            unfcount = 0
            ftotal = 0
            for i in range(9):
                nx, ny = x+dx[i], y+dy[i]
                # if unfilled
                if not grid[nx][ny]:
                    unfcount += 1
                    # count filled neighbors
                    for j in range(9):
                        mx, my = nx+dx[j], ny+dy[j]
                        if grid[mx][my]:
                            ftotal += 1
            if unfcount > 0:
                m_average = ftotal/(unfcount**2)
                if m_average > average:
                    average = m_average
                    bx, by = x, y
            else:
                borders.remove((x, y))

        print(bx, by)
        sys.stdout.flush()

    return True


T = int(input())
for _ in range(T):
    if not solve():
        break
