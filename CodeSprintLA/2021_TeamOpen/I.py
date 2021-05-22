import math

# def ccw(A,B,C):
#     return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

# # Return true if line segments AB and CD intersect
# def intersect(A,B,C,D):
#     return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

def intersectRays(line1, line2):
    ass = line1[0]
    bss = line2[0]
    ad = [line1[1][0]-line1[0][0], line1[1][1]-line1[0][1]]
    bd = [line2[1][0]-line2[0][0], line2[1][1]-line2[0][1]]

    dx = bss[0] - ass[0]
    dy = bss[1] - ass[1]
    det = bd[0] * ad[1] - bd[1] * ad[0]
    if det == 0: return False
    u = (dy * bd[0] - dx * bd[1]) / det
    v = (dy * ad[0] - dx * ad[1]) / det
    return u > 0 and v > 0

def line_intersection(line1, line2):
    if not intersectRays(line1, line2):
        return -1

    # if not intersect(line1[0], line1[1], line2[0], line2[1]):
    #     return -1

    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
       return -1

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return math.floor(x), math.floor(y)

x1,y1,x1s,y1s,x2,y2,x2s,y2s = map(int, input().split())
line1 = ((x1,y1),(x1s,y1s))
line2 = ((x2,y2),(x2s,y2s))
ans = line_intersection(line1, line2)
if ans == -1:
    print(-1)
else:
    x, y = ans
    print(x,y)