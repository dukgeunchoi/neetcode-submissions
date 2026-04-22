class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        valid = set()

        def dfs(r, c):
            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] == "X" or
                (r, c) in valid):
                return
            valid.add((r, c))
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
        
        for r in range(rows):
            print(board[r][cols - 1])
            if board[r][0] == "O":
                print("HELLO")
                dfs(r, 0)
            if board[r][cols - 1] == "O":
                print("HELLO")
                dfs(r, cols - 1)
        
        for c in range(cols):
            if board[0][c] == "O":
                dfs(0, c)
            if board[rows - 1][c] == "O":
                dfs(rows - 1, c)
        
        print(valid)
        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == "O" and 
                    (r, c) not in valid):
                    board[r][c] = "X"
