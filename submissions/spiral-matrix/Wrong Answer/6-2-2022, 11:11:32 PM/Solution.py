// https://leetcode.com/problems/spiral-matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        res = []
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        avail = set()
        i = 0
        j = 0
        while (i < m) and (j < n):
            res.append(matrix[i][j])
            avail.add((i, j))
            flag = False
            for x in range(4):
                next_i = i + dx[x]
                next_j = j + dy[x]
                if (next_i < 0) or (next_j < 0) or (next_i == m) or (next_j == n):
                    continue
                if (next_i, next_j) not in avail:
                    i = next_i
                    j = next_j
                    flag = True
                    break
            if flag is False:
                break
        return res
                 