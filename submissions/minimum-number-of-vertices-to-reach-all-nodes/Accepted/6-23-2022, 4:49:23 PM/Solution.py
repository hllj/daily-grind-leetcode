// https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes

class Solution:
    def dfs(self, u, avail, adj):
        avail[u] = False
        for v in adj[u]:
            if avail[v] is True:
                self.dfs(v, avail, adj)
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = {}
        for i in range(n):
            adj[i] = []
        for edge in edges:
            u, v = edge
            adj[u].append(v)
        avail = [True for _ in range(n)]
        for u in range(n):
            if avail[u] is True:
                for v in adj[u]:
                    self.dfs(v, avail, adj)
        res = []
        for i in range(n):
            if avail[i] is True:
                res.append(i)
        return res