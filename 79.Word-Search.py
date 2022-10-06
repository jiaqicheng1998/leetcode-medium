# Given an m x n grid of characters board and a string word, return true if word exists in the grid.

# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are 
# horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:

# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

def exist(board, word):
    boardDic = defaultdict(int)
    for i in range(len(board)):
        for j in range(len(board[0])):
            boardDic[board[i][j]] += 1
                
    wordDic = Counter(word)
    for c in wordDic:
        if c not in boardDic or boardDic[c] < wordDic[c]:
            return False
            
    ROWS, COLS = len(board), len(board[0])

    def dfs(r,c,i):
        if i == len(word):
            return True
        if (r < 0 or c < 0 or r >= ROWS or c >= COLS #out of bounds
            or word[i] != board[r][c]):  #not what we are looking for
            return False 

        temp = board[r][c]
        board[r][c] = -1
        res = (dfs(r+1, c, i+1)
            or dfs(r-1, c, i+1)
            or dfs(r, c+1, i+1)
            or dfs(r, c-1, i+1))
        board[r][c] = temp
        return res

    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == word[0]:
                if dfs(r,c,0): return True
    return False
