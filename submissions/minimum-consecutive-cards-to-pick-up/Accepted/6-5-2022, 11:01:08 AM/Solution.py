// https://leetcode.com/problems/minimum-consecutive-cards-to-pick-up

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        d = {}
        for i, x in enumerate(cards):
            if x not in d:
                d[x] = [i]
            else:
                d[x].append(i)
        res = int(1e5 + 1)
        for k, v in d.items():
            if len(v) >= 2:
                for i in range(len(v) - 1):
                    res = min(res, v[i + 1] - v[i] + 1)
        if res  == int(1e5 + 1):
            return -1
        return res