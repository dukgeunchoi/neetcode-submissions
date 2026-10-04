class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        islandAreas = []
        rows, cols = len(grid), len(grid[0])

        def bfs(r, c):
            visited.add((r,c))
            q = collections.deque()
            q.append((r,c))
            length = 1

            while q:
                r1, c1 = q.popleft()
                directions = [(-1,0), (1, 0), (0,-1), (0,1)]
                for dr, dc in directions:
                    r2, c2 = r1 + dr, c1 + dc
                    if r2 in range(rows) and c2 in range(cols) and grid[r2][c2] == 1 and (r2,c2) not in visited:
                        visited.add((r2, c2))
                        q.append((r2, c2))
                        length += 1
            
            islandAreas.append(length)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    bfs(r, c)
        
        return max(islandAreas) if islandAreas else 0
        