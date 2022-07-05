// https://leetcode.com/problems/keys-and-rooms

class Solution:
    def dfs(self, u, avail, rooms):
        avail[u] = False
        for v in rooms[u]:
            if avail[v] is True:
                self.dfs(v, avail, rooms)
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        avail = [True for _ in range(n)]
        self.dfs(0, avail, rooms)
        for i in range(n):
            if avail[i] is True:
                return False
        return True
            