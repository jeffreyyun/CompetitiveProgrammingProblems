#!/bin/python3
import time
import queue

def paintFill(a, x, y, newColor):
    X, Y = len(a), len(a[0])    # assumes valid grid
    origColor = a[x][y]
    q = queue.Queue()
    q.put((x,y))
    while not q.empty():
        x,y = q.get()
        a[x][y] = newColor
        for dx,dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            if x+dx >= 0 and y+dy >= 0 and x+dx < X and y+dy < Y and a[x+dx][y+dy] == origColor:
                q.put((x+dx,y+dy))
    return a


def test(inp, case=1):

    def printGrid(grid):
        for r in grid:
            print(r)
        print()

    print("-----TESTING BEGINS-----")
    printGrid(inp[0])

    res = paintFill(*inp)
    printGrid(res)
    return res



if __name__ == '__main__':

    inps =[
    ([[1,1,1,1,1],
    [1,1,2,2,3],
    [1,2,2,3,1],
    [1,2,4,3,3]], 3,4,6)
    ]

    for inp in inps:

        start_time = time.time()
        test(inp, 1)
        t1 = time.time() - start_time

        # start_time = time.time()
        # test(inp, 2)
        # t2 = time.time() - start_time

        # print(t1, t2, t1/t2)
