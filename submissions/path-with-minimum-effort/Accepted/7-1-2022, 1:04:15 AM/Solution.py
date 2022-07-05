// https://leetcode.com/problems/path-with-minimum-effort

class Solution:
    dx = [-1, 0, 1, 0]
    dy = [0, -1, 0, 1]
    def bfs(self, heights, rows, cols, k):
        q = []
        visited = set()
        q.append((0, 0))
        visited.add((0, 0))
        while len(q) > 0:
            u, v = q.pop(0)
            for i in range(4):
                u1, v1 = u + self.dx[i], v + self.dy[i]
                if u1 < 0 or u1 == rows or v1 < 0 or v1 == cols:
                    continue
                if (u1, v1) not in visited and abs(heights[u1][v1] - heights[u][v]) <= k:
                    if u1 == rows - 1 and v1 == cols - 1:
                        return True
                    q.append((u1, v1))
                    visited.add((u1, v1))
        return False
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        # print(rows, cols)
        v_max = max(max(x) for x in heights)
        v_min = min(min(x) for x in heights)
        l = 0
        r = v_max - v_min
        res = r
        # print(self.bfs(heights, rows, cols, 3))
        while l <= r:
            m = (l + r) // 2
            if self.bfs(heights, rows, cols, m):
                res = m
                r = m - 1
            else:
                l = m + 1
        return res