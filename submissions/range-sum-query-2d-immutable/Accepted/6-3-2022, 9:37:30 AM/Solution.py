// https://leetcode.com/problems/range-sum-query-2d-immutable

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.n = len(matrix)
        self.m = len(matrix[0])
        self.matrix = matrix.copy()
        for i in range(1, self.n):
            self.matrix[i][0] += self.matrix[i - 1][0]
        for j in range(1, self.m):
            self.matrix[0][j] += self.matrix[0][j - 1]
        for i in range(1, self.n):
            for j in range(1, self.m):
                self.matrix[i][j] = self.matrix[i][j] + self.matrix[i - 1][j] + self.matrix[i][j - 1] - self.matrix[i - 1][j - 1]
        print(self.matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = self.matrix[row2][col2]
        if col1 - 1 >= 0:
            s -= self.matrix[row2][col1 - 1]
        if row1 - 1 >= 0:
            s -= self.matrix[row1 - 1][col2]
        if row1 - 1 >= 0 and col1 - 1 >= 0:
            s += self.matrix[row1 - 1][col1 - 1]
        return s


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)