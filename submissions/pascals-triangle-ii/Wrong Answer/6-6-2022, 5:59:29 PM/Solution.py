// https://leetcode.com/problems/pascals-triangle-ii

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [[1, 1]]
        res = [[1], [1, 1]]
        for i in range(2, rowIndex + 1):
            row = [1]
            n = len(res[-1])
            last = res[-1]
            for i in range(n - 1):
                row.append(last[i] + last[i + 1])
            row.append(1)
            res.append(row)
        return res[-1]