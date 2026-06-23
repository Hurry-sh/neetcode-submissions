class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        INF = 2147483647

        def bfs(sr, sc):
            q = deque()
            q.append((sr, sc, 0))  # (row, col, distance)
            visit = set()
            visit.add((sr, sc))

            while q:
                r, c, dist = q.popleft()
                if grid[r][c] == 0:  # Found treasure
                    return dist
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visit and grid[nr][nc] != -1:
                        visit.add((nr, nc))
                        q.append((nr, nc, dist + 1))
            return INF  # No treasure found

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == INF:
                    grid[r][c] = bfs(r, c)