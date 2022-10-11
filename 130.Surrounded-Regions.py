# Given an m x n matrix board containing 'X' and 'O', 
# capture all regions that are 4-directionally surrounded 
# by 'X'.

# A region is captured by flipping all 'O's into 'X's in 
# that surrounded region.

def solve(board):
    
    rows, cols = len(board), len(board[0])

    #1.capture unsurrounded regions(o -> t)
    def capture(r,c):
        if (r < 0 or c < 0 or r == rows or c == cols
            or board[r][c] != "O"):
            return
        board[r][c] = "T"
        capture(r+1,c)
        capture(r-1,c)
        capture(r,c+1)
        capture(r,c-1)

    for r in range(rows):
        for c in range(cols):
            if (board[r][c] == "O"
                and (r in [0, rows - 1] or c in [0, cols - 1])):
                capture(r,c)
    #2.capture surrounded regions (o -> x)
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O":
                board[r][c] = "X"
    #3.uncapture unsurrounded regions (t -> o)
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "T":
                board[r][c] = "O"
