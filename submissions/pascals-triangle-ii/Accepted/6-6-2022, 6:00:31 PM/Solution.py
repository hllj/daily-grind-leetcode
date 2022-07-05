// https://leetcode.com/problems/pascals-triangle-ii

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]
        last = [1, 1]
        for i in range(2, rowIndex + 1):
            row = [1]
            n = len(last)
            for i in range(n - 1):
                row.append(last[i] + last[i + 1])
            row.append(1)
            last = row
        return last