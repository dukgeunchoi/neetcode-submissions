class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()

        # find all rotten fruits
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r,c))
        time = 0
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        while q:
            qLen = len(q)
            for i in range(qLen):
                r, c = q.popleft()
                print(r,c)
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1:
                        print(nr,nc)
                        grid[nr][nc] = 2
                        q.append((nr,nc))
            if len(q) > 0: time += 1
        
        return -1 if any(1 in sublists for sublists in grid) else time

