// https://leetcode.com/problems/matchsticks-to-square

class Solution:
    def backtrack(self, i, n, matchsticks, s, edge):
        if self.sol == True:
            return
        if i == n:
            if (edge[0] == edge[1] == edge[2] == edge[3]):
                self.sol = True
            return
        for k in range(4):
            if self.sol == True:
                break
            if (edge[k] + matchsticks[i] <= s // 4):
                edge[k] += matchsticks[i]
                self.backtrack(i + 1, n, matchsticks, s, edge)
                edge[k] -= matchsticks[i]
    def makesquare(self, matchsticks: List[int]) -> bool:
        matchsticks.sort(reverse=True)
        n = len(matchsticks)
        s = sum(matchsticks)
        if s % 4 != 0:
            return False
        edge = [0, 0, 0, 0]
        self.sol = False
        self.backtrack(0, n, matchsticks, s, edge)
        return self.sol