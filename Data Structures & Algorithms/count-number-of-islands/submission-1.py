class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0

        rows, cols = len(grid), len(grid[0])
        visit = set()
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            if (r not in range(rows) or
                c not in range(cols) or
                grid[r][c] != "1" or
                (r, c) in visit):
                return

            visit.add((r, c))
            q.append((r, c))

            bfs(r-1, c)
            bfs(r + 1, c)
            bfs(r, c - 1)
            bfs(r, c + 1)
            # while q:
            #     row, col = q.popleft()
            #     directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

            #     for dr, dc in directions:
            #         r, c = row + dr, col + dc
            #         if (r in range(rows) and
            #             c in range(cols) and
            #             grid[r][c] == "1" and
            #             (r, c) not in visit):
            #             visit.add((r, c))
            #             q.append((r, c ))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1
        
        return islands