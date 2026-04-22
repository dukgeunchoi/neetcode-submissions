class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = defaultdict(list)
        col = defaultdict(list)
        box = defaultdict(list)

        for i, r in enumerate(board):
            for j, c in enumerate(r):
                if c == ".":
                    continue
                boxIndex = (i//3, j//3)

                if c in row[i] or c in col[j] or c in box[boxIndex]:
                    return False
                row[i].append(c)
                col[j].append(c)
                box[boxIndex].append(c)
        return True
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