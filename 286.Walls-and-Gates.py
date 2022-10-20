# You are given an m x n grid rooms initialized with these three possible values.

# -1 A wall or an obstacle.
# 0 A gate.
# INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent 
# INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to 
# reach a gate, it should be filled with INF.

# 1. use bfs, start from the gate, if adjacent is empty, fill in time, terminate after the queue is empty

def wallsAndGates(rooms):
    q = collections.deque()
    ROWS, COLS = len(rooms), len(rooms[0])
    distance = 0

    for r in range(ROWS):
        for c in range(COLS):
            if rooms[r][c] == 0:
                q.append([r,c])
    
    directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            for dr, dc in directions:
                row, col = dr + r, dc + c 
                # if in bound and empty, mark the distance
                if (row < 0 or row >= len(rooms) or
                    col < 0 or col >= len(rooms[0]) or 
                    rooms[row][col] != 2147483647):
                    continue
                rooms[row][col] = distance + 1
                q.append([row, col])
        distance += 1
    
