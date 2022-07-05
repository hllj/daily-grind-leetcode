// https://leetcode.com/problems/jump-game-iv

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        q = [0]
        visited = set()
        visited.add(0)
        f = [0 for _ in range(n)]
        while len(q) > 0:
            i = q.pop(0)
            for j in range(n):
                if ((j == i + 1) or (j == i - 1) or arr[i] == arr[j]) and j not in visited:
                    f[j] = f[i] + 1
                    if j == n - 1:
                        return f[j]
                    q.append(j)
                    visited.add(j)
        return f[n - 1]