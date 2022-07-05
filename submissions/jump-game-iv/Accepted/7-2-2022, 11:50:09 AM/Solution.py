// https://leetcode.com/problems/jump-game-iv

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        q = [0]
        visited = set()
        visited.add(0)
        f = [0 for _ in range(n)]
        s = {}
        for i in range(n):
            if arr[i] not in s:
                s[arr[i]] = [i]
            else:
                s[arr[i]].append(i)
        while len(q) > 0:
            i = q.pop(0)
            for j in s[arr[i]]:
                if j not in visited:
                    f[j] = f[i] + 1
                    if j == n - 1:
                        return f[j]
                    q.append(j)
                    visited.add(j)
            s[arr[i]].clear()
            for j in [i - 1, i + 1]:
                if (0 <= j < n) and j not in visited:
                    f[j] = f[i] + 1
                    if j == n - 1:
                        return f[j]
                    q.append(j)
                    visited.add(j)
        return f[n - 1]