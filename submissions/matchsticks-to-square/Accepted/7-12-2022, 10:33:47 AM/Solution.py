// https://leetcode.com/problems/matchsticks-to-square

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        @lru_cache()
        def rc(idx, a,b,c,d):
            if max(a,b,c,d) > mx:
                return False
            if idx == -1:
                return a == b == c == d
        
            s1 = rc(idx-1, a+matchsticks[idx], b, c, d)
            if s1:
                return True
            s2 = rc(idx-1, a, b+matchsticks[idx], c, d)
            if s2:
                return True
            s3 = rc(idx-1, a, b, c+matchsticks[idx], d)
            if s3:
                return True
            s4 = rc(idx-1, a, b, c, d+matchsticks[idx])
            if s4:
                return True
            return False
        
        matchsticks.sort()
        sm = sum(matchsticks)
        if sm % 4 != 0:
            return False
        mx = sum(matchsticks) / 4
        return rc(len(matchsticks)-2, matchsticks[len(matchsticks)-1],0,0,0)