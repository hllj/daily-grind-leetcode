// https://leetcode.com/problems/spiral-matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        row_begin = 0
        row_end = m - 1
        col_begin = 0
        col_end = n - 1
        res = []
        while row_begin <= row_end and col_begin <= col_end:
            for j in range(col_begin, col_end + 1):
                res.append(matrix[row_begin][j])
            row_begin += 1
            for i in range(row_begin, row_end + 1):
                res.append(matrix[i][col_end])
            col_end -= 1
            for j in range(col_end, col_begin - 1, - 1):
                res.append(matrix[row_end][j])
            row_end -= 1
            for i in range(row_end, row_begin - 1, - 1):
                res.append(matrix[i][col_begin])
            col_begin += 1
        return res
                 