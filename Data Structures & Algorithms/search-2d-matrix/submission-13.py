class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        l, r = 0, row * col - 1
        print(l, r)

        while l <= r:
            m = (l+r) // 2
            curr_col = m % col
            curr_row = m // col
            val = matrix[curr_row][curr_col]
            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return True
        return False