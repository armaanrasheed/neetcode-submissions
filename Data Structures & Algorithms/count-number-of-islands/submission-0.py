from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        ROWS = len(grid)
        COLS = len(grid[0])
        result = 0
        visited = set()
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == '1' and (row, col) not in visited:
                    result += 1
                    q = deque([(row, col)])
                    visited.add((row, col))
                    
                    while q:
                        r, c = q.popleft()
                        
                        for dr, dc in directions:
                            nr = r + dr
                            nc = c + dc
                            
                            if (0 <= nr < ROWS and 
                                0 <= nc < COLS and 
                                (nr, nc) not in visited and 
                                grid[nr][nc] == '1'):
                                visited.add((nr, nc))
                                q.append((nr, nc))
        
        return result