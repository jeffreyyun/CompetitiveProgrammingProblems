#!/bin/python3
import math
import time


def eightQueens(N=8):
    print("Initializing on {} by {} grid".format(N, N))
    grid = [[0 for i in range(N)] for j in range(N)]
    # using set is actually not necessary here
    resSet = set()
    placed = [None for i in range(N)]  # the column where queen is placed
    placeQueen(grid, resSet, placed)
    return resSet

def placeQueen(grid, resSet, placed, row=0):
    # place Queens row by row
    N = len(grid)
    if row == N:
        stringified = '\n'.join([ ''.join( [str(x) for x in grid[i]] ) for i in range(N) ])
        resSet.add(stringified)
        return
    for col in range(N):
        if (check(grid, row, col, placed)):
            placed[row] = col
            grid[row][col] = 1
            placeQueen(grid, resSet, placed, row+1)
            grid[row][col] = 0
            placed[row] = None
    return

def check(grid, row1, col1, placed):
    for row2 in range(row1):
        col2 = placed[row2]
        if col2 == None:
            continue
        # checks the column
        if col2 == col1:
            return False
        # checks the diagonal
        if abs(row2-row1) == abs(col2-col1):
            return False
    return True


def printGrid(grid, ct=99):
    for r in grid:
        ct -= 1
        if ct <= 0:
            break
        print(r)
        print()
    print()
    print("Total Elements: ", len(grid) )

def test(inp, case=1):

    print("-----TESTING BEGINS-----")
    res = eightQueens()
    printGrid(res)

    return res



if __name__ == '__main__':

    inps = [0]

    for inp in inps:

        start_time = time.time()
        test(inp, 1)
        t1 = time.time() - start_time
        print(t1)