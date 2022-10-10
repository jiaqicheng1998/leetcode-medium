# You are given an m x n binary matrix grid. An island is a group of 1's (representing land)
#  connected 4-directionally (horizontal or vertical.) You may assume all four edges of the 
#  grid are surrounded by water.

# The area of an island is the number of cells with a value 1 in the island.

# Return the maximum area of an island in grid. If there is no island, return 0.

def maxAreaOfIsland(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    visited = set()
    areas = []

    def bfs(r,c,area):
        q = collections.deque()
        visited.add((r,c))
        q.append((r,c))

        while q:
            row, col = q.popleft()
            directions = [[1,0], [-1,0], [0,1], [0,-1]]

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if (r in range(rows) and
                    c in range(cols) and
                    grid[r][c] == 1 and
                    (r,c) not in visited):
                    q.append((r,c))
                    visited.add((r,c))
                    area += 1
        
        return area 

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1 and (r,c) not in visited:
                areas.append(bfs(r,c,1))
    
    if areas:
        return max(areas)
    else:
        return 0


grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]]

print(maxAreaOfIsland(grid))