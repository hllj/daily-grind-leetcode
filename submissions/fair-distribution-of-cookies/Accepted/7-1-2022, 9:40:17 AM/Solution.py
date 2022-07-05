// https://leetcode.com/problems/fair-distribution-of-cookies

class Solution:
    def backtrack(self, i, n, x, cookies, dis, k):
        if i == n:
            # print(x, dis, max(dis))
            self.res = min(self.res, max(dis))
        else:
            for t in range(k):
                if dis[t] + cookies[i] < self.res:
                    x[i] = t
                    dis[t] += cookies[i]
                    self.backtrack(i + 1, n, x, cookies, dis, k)
                    x[i] = -1
                    dis[t] -= cookies[i]
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        n = len(cookies)
        self.res = 8 * int(1e5 + 1)
        x = [-1 for _ in range(n)]
        dis = [0 for _ in range(k)]
        self.backtrack(0, n, x, cookies, dis, k)
        return self.res