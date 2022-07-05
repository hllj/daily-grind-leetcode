// https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        i = 0
        j = n - 1
        cnt = 0
        res = 0
        while cnt < k:
            if cardPoints[i] > cardPoints[j]:
                res += cardPoints[i]
                i += 1
            else:
                res += cardPoints[j]
                j -= 1
            cnt += 1
        return res