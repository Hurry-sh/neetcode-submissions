
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        count = 0
        q = collections.deque()
        
        # count fresh oranges and enqueue all rotten ones
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    count += 1
                if grid[i][j] == 2:
                    q.append((i, j, 0))   # rotten start points with level 0

        def bfs(count, level):
            nonlocal q
            while q:
                row, col, lvl = q.popleft()
                level = max(level, lvl)  # track the latest minute
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                        grid[r][c] = 2       # rot the fresh orange
                        count -= 1
                        q.append((r, c, lvl + 1))
            return -1 if count > 0 else level

        return bfs(count, 0)
