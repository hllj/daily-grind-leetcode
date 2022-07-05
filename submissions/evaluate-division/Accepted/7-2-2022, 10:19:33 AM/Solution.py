// https://leetcode.com/problems/evaluate-division

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = {}
        weight = {}
        for equation, v in zip(equations, values):
            a, b = equation
            if a not in adj:
                adj[a] = [a, b]
            else:
                adj[a].append(a)
                adj[a].append(b)
            if b not in adj:
                adj[b] = [a, b]
            else:
                adj[b].append(a)
                adj[b].append(b)
            weight[(a, a)] = 1.0
            weight[(a, b)] = v
            weight[(b, b)] = 1.0
            weight[(b, a)] = 1.0 / v
        inf = float('inf')
        res = []
        for query in queries:
            s, t = query
            if s not in adj.keys() or t not in adj.keys():
                res.append(-1)
                continue
            f = {}
            n = len(adj.keys())
            for u in adj.keys():
                f[u] = inf
            f[s] = 1
            visited = set()
            for i in range(n):
                u_best = None
                d_best = inf
                for u in adj.keys():
                    if f[u] < d_best and u not in visited:
                        u_best = u
                        d_best = f[u]
                # print('u best', u_best)
                if u_best == t:
                    break
                u = u_best
                visited.add(u)
                for v in adj.keys():
                    if (u, v) in weight:
                        # print(u, v, weight[(u, v)], f[u], f[v])
                        f[v] = min(f[v], f[u] * weight[(u, v)])
                # print(f)
            if f[t] == inf:
                res.append(-1)
            else:
                res.append(f[t])
        return res
            
            