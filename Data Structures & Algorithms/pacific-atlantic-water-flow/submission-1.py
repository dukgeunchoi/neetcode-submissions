class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pac, atl = set(), set()
        res = []
        rows, cols = len(heights), len(heights[0])

        def dfs(r, c, flowable, prev):
            if r not in range(rows) or c not in range(cols) or heights[r][c] < prev or (r,c) in flowable:
                return
            flowable.add((r,c))
            dfs(r - 1, c, flowable, heights[r][c]) 
            dfs(r + 1, c, flowable, heights[r][c]) 
            dfs(r, c-1, flowable, heights[r][c]) 
            dfs(r, c+1, flowable, heights[r][c]) 

        for r in range(rows):
            dfs(r, 0, pac, 0)
            dfs(r, cols - 1, atl, 0)

        for c in range(cols):
            dfs(0, c, pac, 0)
            dfs(rows - 1, c, atl, 0)
        
        for r in range(rows):
            for c in range(cols):
                if (r,c)in pac and (r,c) in atl:
                    res.append([r,c])
        
        return res
        