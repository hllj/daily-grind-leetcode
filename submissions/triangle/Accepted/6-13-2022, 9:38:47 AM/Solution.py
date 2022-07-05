// https://leetcode.com/problems/triangle

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        for i in range(1, n):
            for j in range(i + 1):
                can = []
                if 0 <= j <= i - 1:
                    can.append(triangle[i - 1][j])
                if 0 <= j - 1 <= i - 1:
                    can.append(triangle[i - 1][j - 1])
                triangle[i][j] += min(can)
                    
        return min(triangle[-1])