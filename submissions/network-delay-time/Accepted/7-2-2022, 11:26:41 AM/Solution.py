// https://leetcode.com/problems/network-delay-time

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1, n + 1):
            adj[i] = []
        weight = {}
        for time in times:
            u, v, w = time
            adj[u].append(v)
            weight[(u, v)] = w
        inf = float('inf')
        f = {}
        for i in range(1, n + 1):
            f[i] = inf
        f[k] = 0
        visited = set()
        for i in range(n):
            u_best = None
            d_best = inf
            for u in range(1, n + 1):
                if f[u] < d_best and u not in visited:
                    u_best = u
                    d_best = f[u]
            # print('choose', u_best)
            if u_best == None:
                break
            u = u_best
            visited.add(u)
            for v in range(1, n + 1):
                if (u, v) in weight:
                    f[v] = min(f[v], f[u] + weight[(u, v)])
            # print(f)
        res = 0
        for i in range(1, n + 1):
            if i != k:
                if f[i] == inf:
                    return -1
                else:
                    res = max(res, f[i])
        return res