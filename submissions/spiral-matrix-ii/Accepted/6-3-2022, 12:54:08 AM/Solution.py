// https://leetcode.com/problems/spiral-matrix-ii

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        idx = 1
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        row_begin = 0
        row_end = n - 1
        col_begin = 0
        col_end = n - 1
        while row_begin <= row_end and col_begin <= col_end:
            for j in range(col_begin, col_end + 1):
                matrix[row_begin][j] = idx
                idx += 1
            row_begin += 1
            if row_begin > row_end or col_begin > col_end:
                break
            for i in range(row_begin, row_end + 1):
                matrix[i][col_end] = idx
                idx += 1
            col_end -= 1
            if row_begin > row_end or col_begin > col_end:
                break
            for j in range(col_end, col_begin - 1, -1):
                matrix[row_end][j] = idx
                idx += 1
            row_end -= 1
            if row_begin > row_end or col_begin > col_end:
                break
            for i in range(row_end, row_begin - 1, -1):
                matrix[i][col_begin] = idx
                idx += 1
            col_begin += 1
        return matrix