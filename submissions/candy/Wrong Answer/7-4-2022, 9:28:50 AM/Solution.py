// https://leetcode.com/problems/candy

import heapq
class Solution:
    def candy(self, ratings: List[int]) -> int:
        li = []
        for idx, rating in enumerate(ratings):
            li.append((rating, idx))
        heapq.heapify(li)
        n = len(ratings)
        res = [0 for _ in range(n)]
        while len(li):
            rating, idx = li[0]
            heapq.heappop(li)
            v_max = 0
            r_max = 0
            if (idx - 1 >= 0):
                if res[idx - 1] != 0:
                    v_max = max(v_max, ratings[idx - 1])
                r_max = max(r_max, res[idx - 1])
            if (idx + 1 < n):
                if res[idx + 1] != 0:
                    v_max = max(v_max, ratings[idx + 1])
                r_max = max(r_max, res[idx + 1])
            # print(rating, idx, r_max, v_max)
            if r_max == 0:
                res[idx] = 1
            elif v_max == rating:
                res[idx] = r_max - 1
            else:
                res[idx] = r_max + 1
                
        print(res)
        return sum(res)