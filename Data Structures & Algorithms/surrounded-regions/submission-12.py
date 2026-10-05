class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        valid = set()
        borderRegions = []

        for r in range(rows):
            if board[r][0] == "O":
                borderRegions.append((r,0))
            if board[r][cols-1] == "O":
                borderRegions.append((r, cols-1))

        for c in range(cols):
            if board[0][c]  == "O":
                borderRegions.append((0, c))
            if  board[rows-1][c] == "O":
                borderRegions.append((rows-1, c))
        
        def dfs(r, c):
            if r not in range(rows) or c not in range(cols) or board[r][c] == "X" or (r,c) in valid:
                return
            valid.add((r,c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c-1)
            dfs(r, c+1)

        for r, c in borderRegions:
            dfs(r, c)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and (r,c) not in valid:
                    board[r][c] = "X"
        return