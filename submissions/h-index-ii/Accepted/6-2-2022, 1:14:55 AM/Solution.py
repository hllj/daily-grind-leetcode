// https://leetcode.com/problems/h-index-ii

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        l1 = 0
        r1 = 1000
        res = 0
        while l1 <= r1:
            m1 = (l1 + r1) // 2
            l2 = 0
            r2 = n - 1
            idx = -1
            while l2 <= r2:
                m2 = (l2 + r2) // 2
                if citations[m2] >= m1:
                    idx = m2
                    r2 = m2 - 1
                else:
                    l2 = m2 + 1
            print('check', m1, idx)
            cnt = n - idx if idx != -1 else 0
            if cnt >= m1:
                res = m1
                l1 = m1 + 1
            else:
                r1 = m1 - 1
            # cnt = 0
            # for x in citations:
            #     if x >= m1:
            #         cnt += 1
            # if cnt >= m1:
            #     res = m1
            #     l1 = m1 + 1
            # else:
            #     r1 = m1 - 1
        return res