// https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        if matrix[0][0] > target or matrix[n - 1][m - 1] < target:
            return False
        for i in range(n):
            arr = matrix[i]
            if arr[0] > target or arr[m - 1] < target:
                continue
            l = 0
            r = m - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid] == target:
                    return True
                if arr[mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
        return False