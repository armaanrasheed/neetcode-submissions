from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        directions = ((-1,0),(1,0),(0,-1),(0,1))
        max_area = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    q = deque([(row, col)])
                    visited.add((row, col))
                    area = 1

                    while q:
                        r, c = q.popleft()
                        for dr, dc in directions:
                            nr, nc = r + dr, c + dc
                            if (
                                0 <= nr < ROWS and
                                0 <= nc < COLS and
                                grid[nr][nc] == 1 and
                                (nr, nc) not in visited
                            ):
                                visited.add((nr, nc))
                                area += 1
                                q.append((nr, nc))

                    max_area = max(max_area, area)

        return max_area