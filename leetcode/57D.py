class Solution:
    def candyCrush(self, board):
        """
        :type board: List[List[int]]
        :rtype: List[List[int]]
        """
        def printGrid(board):
            for r in board:
                print(''.join([str(c) + "\t" for c in r]))
            print()

        def checkCrush_col(i, j, rows, cols):
            val = board[i][j]
            if val == 0:
                return False
            if (board[i+1][j] == val and board[i+2][j] == val):
                grid[i][j] = 0
                grid[i+1][j] = 0
                grid[i+2][j] = 0
                for i2 in range(i+3,rows):
                    if board[i2][j] == val:
                        grid[i2][j] = 0
                    else:
                        break
                return True

        def checkCrush_row(i,j, row, cols):
            val = board[i][j]
            if val == 0:
                return False
            if (board[i][j+1] == val and board[i][j+2] == val):
                grid[i][j] = 0
                grid[i][j+1] = 0
                grid[i][j+2] = 0
                for j2 in range(j+3,cols):
                    if board[i][j2] == val:
                        grid[i][j2] = 0
                    else:
                        break
                return True

        rows = len(board)
        cols = len(board[0])
        crushed = True

        while crushed:
            crushed = False
            grid = copy.deepcopy(board)

            for r in range(rows-2):
                for c in range(cols):
                    if checkCrush_col(r,c,rows,cols):
                        crushed = True

            for r in range(rows):
                for c in range(cols-2):
                    if checkCrush_row(r,c,rows,cols):
                        crushed = True

            for c in range(cols):
                for r in range(rows-1, 0, -1):
                    if grid[r][c] == 0:
                        diff = 0
                        # find new bottom block
                        for r2 in range(r, -1, -1):
                            if grid[r2][c] != 0:
                                diff = r - r2
                                break
                        if diff == 0:   # entire column zero
                            break
                        # shift blocks downward
                        for r2 in range(r, -1+diff, -1):
                            grid[r2][c] = grid[r2-diff][c]
                        # zero the top blocks displaced
                        for r3 in range(0, diff):
                            grid[r3][c] = 0

            #printGrid(grid)
            board = grid

        return board
