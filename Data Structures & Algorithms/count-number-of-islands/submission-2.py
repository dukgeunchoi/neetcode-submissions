class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def bfs(idx):
            visited.add(idx)
            q = collections.deque()
            q.append(idx)
            while q:
                qLen = len(q)
                for i in range(qLen):
                    row, col = q.popleft()
                    directions = [[1,0], [-1, 0], [0, 1], [0, -1]]
                    for dr, dc in directions:
                        r, c = row + dr, col + dc

                        if r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r,c) not in visited:
                            visited.add((r,c))
                            q.append((r,c))
        
        lands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs((r, c))
                    lands += 1
        
        return lands
                    
