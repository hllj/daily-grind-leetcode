// https://leetcode.com/problems/count-asterisks

class Solution:
    def countAsterisks(self, s: str) -> int:
        pos = s.split('|')
        res = 0
        for i, x in enumerate(pos):
            if i % 2 == 0:
                res += x.count('*')
        return res