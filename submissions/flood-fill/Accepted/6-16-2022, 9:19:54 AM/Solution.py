// https://leetcode.com/problems/flood-fill

class Solution:
    paint = []
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    def dfs(self, image, x, y, n, m, paint, avail):
        avail[x][y] = False
        paint.append((x, y))
        for k in range(4):
            x1, y1 = x + self.dx[k], y + self.dy[k]
            if (x1 < 0) or (x1 == n) or (y1 < 0) or (y1 == m):
                continue
            if image[x1][y1] == image[x][y] and avail[x1][y1] is True:
                self.dfs(image, x1, y1, n, m, paint, avail)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        paint = []
        n = len(image)
        m = len(image[0])
        avail = [[True for _ in range(m)] for _ in range(n)]
        self.dfs(image, sr, sc, n, m, paint, avail)
        for (x, y) in paint:
            image[x][y] = newColor
        return image