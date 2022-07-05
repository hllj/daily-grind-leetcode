// https://leetcode.com/problems/search-a-2d-matrix-ii

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        l1 = 0
        r1 = n - 1
        while l1 <= r1:
            mid = (l1 + r1) // 2
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                r1 = mid - 1
            else:
                l1 = mid + 1
        print(max(0, r1 - 1), min(n, l1 + 1))
        for i in range(max(0, r1 - 1), min(n, l1 + 1)):
            print('matrix', matrix[i])
            l2 = 0
            r2 = m - 1
            while l2 <= r2:
                mid = (l2 + r2) // 2
                if matrix[mid][i] == target:
                    print('found', mid, i)
                    return True
                if matrix[mid][i] > target:
                    r2 = mid - 1
                else:
                    l2 = mid + 1
        return False