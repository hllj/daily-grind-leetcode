// https://leetcode.com/problems/course-schedule

from collections import deque

class Solution:
    def dfs(self, u, visited, sorted_nodes, adj):
        if self.solution is False:
            return
        visited.add(u)
        for v in adj[u]:
            if v not in visited:
                self.dfs(v, visited, sorted_nodes, adj)
        for v in adj[u]:
            if v not in sorted_nodes:
                self.solution = False
                break
        sorted_nodes.appendleft(u)
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for x in prerequisites:
            a, b = x
            adj[b].append(a)
        self.solution = True
        sorted_nodes = deque()
        visited = set()
        for i in range(numCourses):
            if self.solution is False:
                return False
            if i not in visited:
                self.dfs(i, visited, sorted_nodes, adj)
            
        return True