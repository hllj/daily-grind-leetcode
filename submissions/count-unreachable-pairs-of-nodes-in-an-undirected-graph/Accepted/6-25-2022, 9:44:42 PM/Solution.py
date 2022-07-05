// https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph

class Solution:
    def dfs(self, u, visited, adj, group):
        visited.add(u)
        group.append(u)
        for v in adj[u]:
            if v not in visited:
                self.dfs(v, visited, adj, group)
        
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        adj = {}
        for i in range(n):
            adj[i] = []
        for edge in edges:
            u, v = edge
            adj[u].append(v)
            adj[v].append(u)
        visited = set()
        cnt = 0
        for u in range(n):
            if u not in visited:
                group = []
                self.dfs(u, visited, adj, group)
                cnt += (n - len(group)) * len(group)
                # print('u', group)
        return cnt // 2