// https://leetcode.com/problems/transpose-matrix

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        res = []
        for j in range(m):
            transpose = []
            for i in range(n):
                transpose.append(matrix[i][j])
            res.append(transpose)
        return res