// https://leetcode.com/problems/best-sightseeing-pair

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        first = []
        second = []
        for idx, x in enumerate(values):
            first.append(x + idx)
            second.append(x - idx)
        res = 0
        max_first = first[0]
        for i in range(1, len(values)):
            res = max(res, max_first + second[i])
            max_first = max(max_first, first[i])
        return res
        