class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(list)
        cols = defaultdict(list)
        box = defaultdict(list)
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".": continue
                if val in rows[r]: return False
                if val in cols[c]: return False
                if val in box[(r//3, c//3)]: return False
                rows[r].append(val)
                cols[c].append(val)
                box[(r//3, c//3)].append(val)

        return True
