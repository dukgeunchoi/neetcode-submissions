class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = len(board)
        col = len(board[0])

        rows = defaultdict(list)
        cols = defaultdict(list)
        subboxes = defaultdict(list)

        for r in range(row):
            for c in range(col):
                if board[r][c] == ".": continue
                val = board[r][c]
                s1 = r // 3
                s2 = c // 3
                if val in rows[r] or val in cols[c] or val in subboxes[(s1, s2)]:
                    return False
                
                rows[r].append(val)
                cols[c].append(val)
                subboxes[(s1, s2)].append(val)

        return True

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # row = defaultdict(list)
        # col = defaultdict(list)
        # subbox = defaultdict(list)

        # rows, cols = len(board), len(board[0])
        # for r in range(rows):
        #     for c in range(cols):
        #         if board[r][c] == ".":
        #             continue
                
        #         sr = r // 3
        #         sc = c // 3
                
        #         if (board[r][c] in row[r] or
        #             board[r][c]in col[c] or
        #             board[r][c] in subbox[(sr, sc)]):
        #             return False
                
        #         row[r].append(board[r][c])
        #         col[c].append(board[r][c])
        #         subbox[(sr, sc)].append(board[r][c])
        
        # return True
