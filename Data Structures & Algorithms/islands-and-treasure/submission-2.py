class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            q = collections.deque()
            q.append((r,c))

            dist = 0
            while q:
                qLen = len(q)
                dist += 1
                for i in range(qLen):
                    row, col = q.popleft()
                    directions = [(-1, 0), (1,0), (0,-1), (0,1)]
                    for dr,dc in directions:
                        nr, nc = row + dr, col + dc
                        if (nr in range(rows) and nc in range(cols) 
                        and grid[nr][nc] != -1 and grid[nr][nc] > dist):
                            q.append((nr, nc))
                            grid[nr][nc] = dist


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    bfs(r,c)