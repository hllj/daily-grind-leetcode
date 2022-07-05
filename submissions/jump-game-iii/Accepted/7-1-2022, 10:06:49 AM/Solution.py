// https://leetcode.com/problems/jump-game-iii

class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        q = [start]
        visited = set()
        visited.add(start)
        while len(q) > 0:
            u = q.pop(0)
            if arr[u] == 0:
                return True
            if 0 <= u + arr[u] < n and (u + arr[u] not in visited):
                q.append(u + arr[u])
                visited.add(u + arr[u])
            if 0 <= u - arr[u] < n and (u - arr[u] not in visited):
                q.append(u - arr[u])
                visited.add(u - arr[u])
        return False