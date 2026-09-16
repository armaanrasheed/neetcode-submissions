from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        keep track of
            # of rows
            # of columns
            visited = set()
            q = deque()
        '''
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        q = deque()
        numOfIslands = 0
        directions = ((-1,0),(0,1),(1,0),(0,-1))

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    visited.add((row,col))
                    q.append((row,col))
                    numOfIslands+=1

                    while q:
                        r, c = q.popleft()
                        for dr,dc in directions:
                            nr, nc = r + dr, c + dc

                            if (0 <= nr < ROWS and
                            0 <= nc < COLS and
                            (nr, nc) not in visited and
                            grid[nr][nc] == "1"):
                                visited.add((nr, nc))
                                q.append((nr, nc))
        return numOfIslands




