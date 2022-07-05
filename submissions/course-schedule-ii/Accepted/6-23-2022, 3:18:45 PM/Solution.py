// https://leetcode.com/problems/course-schedule-ii

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
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
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
                return []
            if i not in visited:
                self.dfs(i, visited, sorted_nodes, adj)
        return sorted_nodes