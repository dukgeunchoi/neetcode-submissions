class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()
        fresh = 0
        # finding rotten fruits, number of fresh fruits
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        def checkAdjFruit(r, c):
            nonlocal fresh
            if (r not in range(rows) or
                c not in range(cols) or
                grid[r][c] != 1):
                return
            
            q.append((r, c))
            grid[r][c] = 2
            fresh -= 1
        
        minute = 0
        while q and fresh > 0:
            qLen = len(q)
            for i in range(qLen):
                r, c = q.popleft()
                checkAdjFruit(r - 1, c)
                checkAdjFruit(r + 1, c)
                checkAdjFruit(r, c - 1)
                checkAdjFruit(r, c + 1)
            minute += 1
        
        return minute if fresh == 0 else -1
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        


        
        
        
        
        
        # rows, cols = len(grid), len(grid[0])
        # q = collections.deque()
        # time = 0
        # freshFruits = 0

        # def rotFruit(r, c):
        #     nonlocal freshFruits
        #     if (r < 0 or r >= rows or
        #         c < 0 or c >= cols or
        #         grid[r][c] != 1):
        #         return
            
        #     q.append((r, c))
        #     grid[r][c] = 2
        #     freshFruits -= 1
        #     return

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1:
        #             freshFruits += 1
        #         elif grid[r][c] == 2:
        #             q.append((r, c))

        # while q and freshFruits > 0:
        #     print(time, q)
        #     for i in range(len(q)):
        #         r, c = q.popleft()

        #         rotFruit(r + 1, c)
        #         rotFruit(r - 1, c)
        #         rotFruit(r, c + 1)
        #         rotFruit(r, c - 1)
        #     time += 1

        # return time if freshFruits == 0 else -1
