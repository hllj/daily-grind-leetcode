// https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        if k == n:
            return sum(cardPoints)
        left = [0 for _ in range(n)]
        right = [0 for _ in range(n)]
        left[0] = cardPoints[0]
        for i in range(1, n):
            left[i] = left[i - 1] + cardPoints[i]
        right[n - 1] = cardPoints[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] + cardPoints[i]
        res = 0
        for i in range(0, k + 1):
            s = 0
            if i == 0:
                s += right[n - (k - i)]
            elif i == k:
                s += left[i - 1]
            else:
                s += left[i - 1] + right[n - (k - i)]
            # print(s)
            res = max(res, s)
        return res
        