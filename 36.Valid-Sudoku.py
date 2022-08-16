# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells 
# need to be validated according to the following rules:

# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the 
# digits 1-9 without repetition.
# Note:

# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.

from collections import defaultdict
def isValidSudoku(board):
    for i in board:
        set_i = list(set(i))
        temp = []
        for j in i:
            if j != ".":
                temp.append(j)
        if len(set_i) - 1 != len(temp):
            return False
    
    for col in range(len(board[0])):
        set_col = []
        temp_col = []
        for row in range(len(board)):
            set_col.append(board[row][col])
            if board[row][col] != '.':
                temp_col.append(board[row][col])
        if len(list(set(set_col))) - 1 != len(temp_col):
            return False

    d = defaultdict(set)
    for row in range(len(board)):
        for col in range(len(board[0])):
            position = [row // 3, col // 3]
            if board[row][col] != '.' and board[row][col] in d[str(position)]:
                return False
            else: 
                d[str(position)].add(board[row][col])

    return True

board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))