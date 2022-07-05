// https://leetcode.com/problems/number-of-provinces

class Solution:
    def dfs(self, u, visited, adj):
        visited.add(u)
        for v in adj[u]:
            if v not in visited:
                self.dfs(v, visited, adj)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        adj = {}
        for i in range(n):
            adj[i] = []
            for j in range(n):
                if isConnected[i][j] == 1:
                    adj[i].append(j)
        visited = set()
        cnt = 0
        for i in range(n):
            if i not in visited:
                cnt += 1
                self.dfs(i, visited, adj)
        return cnt