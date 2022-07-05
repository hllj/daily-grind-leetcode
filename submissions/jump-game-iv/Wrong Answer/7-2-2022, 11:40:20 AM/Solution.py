// https://leetcode.com/problems/jump-game-iv

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        q = [0]
        visited = set()
        visited.add(0)
        while len(q) > 0:
            i = q.pop(0)
            for j in range(n):
                if (j == i + 1) or (j == i - 1) or arr[i] == arr[j]:
                    if j == n - 1:
                        return True
                    q.append(j)
                    visited.add(j)
        return False