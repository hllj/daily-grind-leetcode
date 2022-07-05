// https://leetcode.com/problems/transpose-matrix

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        transpose = [[0] * n] * m
        res = []
        for j in range(m):
            for i in range(n):
                transpose[j][i] = matrix[i][j]
                print(transpose)
        return res