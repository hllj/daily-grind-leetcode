// https://leetcode.com/problems/pascals-triangle

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1], [1, 1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        for i in range(2, numRows):
            row = [1]
            n = len(res[-1])
            last = res[-1]
            for i in range(n - 1):
                row.append(last[i] + last[i + 1])
            row.append(1)
            res.append(row)
        return res