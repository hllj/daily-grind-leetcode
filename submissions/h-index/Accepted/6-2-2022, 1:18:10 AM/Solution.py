// https://leetcode.com/problems/h-index

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l1 = 0
        r1 = 1000
        res = 0
        while l1 <= r1:
            m1 = (l1 + r1) // 2
            cnt = 0
            for x in citations:
                if x >= m1:
                    cnt += 1
            if cnt >= m1:
                res = m1
                l1 = m1 + 1
            else:
                r1 = m1 - 1
        return res