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
                
                s1 = r // 3
                s2 = c // 3
                if board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in subboxes[(s1, s2)]:
                    return False
                
                rows[r].append(board[r][c])
                cols[c].append(board[r][c])
                subboxes[(s1, s2)].append(board[r][c])

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
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # row = defaultdict(list)
        # col = defaultdict(list)
        # box = defaultdict(list)

        # for i, r in enumerate(board):
        #     for j, c in enumerate(r):
        #         if c == ".":
        #             continue
        #         boxIndex = (i//3, j//3)

        #         if c in row[i] or c in col[j] or c in box[boxIndex]:
        #             return False
        #         row[i].append(c)
        #         col[j].append(c)
        #         box[boxIndex].append(c)
        # return True
                # if i < 3:
                #     if j < 3:
                #         boxIndex = 0
                #     elif j < 6:
                #         boxIndex = 1
                #     else:
                #         boxIndex = 2    
                # elif i < 6:
                #     if j < 3:
                #         boxIndex = 3
                #     elif j < 6:
                #         boxIndex = 4
                #     else:
                #         boxIndex = 5  
                # else:
                #     if j < 3:
                #         boxIndex = 6
                #     elif j < 6:
                #         boxIndex = 7
                #     else:
                #         boxIndex = 8