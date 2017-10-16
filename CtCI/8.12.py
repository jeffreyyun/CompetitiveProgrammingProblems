#!/bin/python3
import math
import time


def eightQueens(N=12):
    print("Initializing on {} by {} grid".format(N, N))
    grid = [[0 for i in range(N)] for j in range(N)]
    resSet = set()
    placeQueen(grid, resSet)
    return resSet

def placeQueen(grid, resSet, row=0):
    # place Queens row by row
    N = len(grid)
    if row == N:
        stringified = '\n'.join([ ''.join( [str(x) for x in grid[i]] ) for i in range(N) ])
        resSet.add(stringified)
        return
    for col in range(N):
        if (check(grid, row, col)):
            grid[row][col] = 1
            placeQueen(grid, resSet, row+1)
            grid[row][col] = 0
    return

def check(grid, row, col):
    N = len(grid)
    # checks the column
    for i in range(N):
        if grid[i][col] == 1:
            return False
    # checks the diagonal
    for i in range(-(N-1),N):
        if checkBounds(N, row+i, col+i) and grid[row+i][col+i]:
            return False
        if checkBounds(N, row+i, col-i) and grid[row+i][col-i]:
            return False
    return True

def checkBounds(N, row, col):
    if row < 0 or col < 0 or row > N-1 or col > N-1:
        return False
    else:
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