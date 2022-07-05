// https://leetcode.com/problems/maximum-total-importance-of-roads

class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        m = len(roads)
        cnt = [0] * n
        for i in range(m):
            a, b = roads[i]
            cnt[a] += 1
            cnt[b] += 1
        print(cnt)
        li = []
        for i, v in enumerate(cnt):
            li.append({
                'i': i,
                'v': v
            })
        li = sorted(li, key=lambda x: x['v'], reverse=True)
        res = 0
        p = n
        for i in range(n):
            res += li[i]['v'] * p
            p -= 1
        return res