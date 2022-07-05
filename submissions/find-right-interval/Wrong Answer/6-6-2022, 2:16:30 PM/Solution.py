// https://leetcode.com/problems/find-right-interval

import functools
class Solution:
    
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        def compare(r1, r2):
            if r1['interval'][0] != r2['interval'][0]:
                if r1['interval'][0] < r2['interval'][0]:
                    return -1
                elif r1['interval'][0] > r2['interval'][0]:
                    return 1
                else:
                    return 0
                
            else:
                if r2['interval'][1] < r2['interval'][1]:
                    return -1
                elif r2['interval'][1] > r2['interval'][1]:
                    return 1
                else:
                    return 0
        n = len(intervals)
        rs = []
        for idx, interval in enumerate(intervals):
            rs.append({'idx': idx, 'interval': interval})
        rs.sort(key=functools.cmp_to_key(compare))
        res = [-1] * n
        for i in range(n):
            interval = rs[i]['interval']
            l = i + 1
            r = n - 1
            idx = -1
            while l <= r:
                m = (l + r) // 2
                if rs[m]['interval'][0] >= interval[1]:
                    idx = rs[m]['idx']
                    r = m - 1
                else:
                    l = m + 1
            res[rs[i]['idx']] = idx
        return res