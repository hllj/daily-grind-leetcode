// https://leetcode.com/problems/swim-in-rising-water

class Solution:
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    def bfs(self, grid, n, k):
        q = []
        visited = set()
        q.append((0, 0))
        visited.add((0, 0))
        while len(q) > 0:
            u, v = q.pop(0)
            for i in range(4):
                u1, v1 = u + self.dx[i], v + self.dy[i]
                if u1 < 0 or u1 == n or v1 < 0 or v1 == n:
                    continue
                if (u1, v1) not in visited and grid[u1][v1] <= k and grid[u][v] <= k:
                    if u1 == n - 1 and v1 == n - 1:
                        return True
                    q.append((u1, v1))
                    visited.add((u1, v1))
        return False
                
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        r = max(max(x) for x in grid)
        l = min(min(x) for x in grid)
        # print(l, r)
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if self.bfs(grid, n, mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res