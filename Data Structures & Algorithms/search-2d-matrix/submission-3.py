class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        height = len(matrix)
        width = len(matrix[0])

        l, r = 0, height * width - 1

        while l <= r:
            m = (l + r) // 2
            row = m // width
            col = m % width
            mid = matrix[row][col]
            if mid < target:
                l = m + 1
            elif mid > target:
                r = m - 1
            else:
                return True

        return False