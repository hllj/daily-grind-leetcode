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
            equal = False
            r_max = 0
            if (idx - 1 >= 0):
                r_max = max(r_max, res[idx - 1])
                equal = equal or (res[idx - 1] != 0 and ratings[idx - 1] < rating)
            if (idx + 1 < n):
                r_max =max(r_max, res[idx + 1])
                equal = equal or (res[idx + 1] != 0 and ratings[idx +1] < rating)
            print(rating, idx, r_max, equal)
            if r_max == 0:
                res[idx] = 1
            elif equal:
                res[idx] = r_max + 1
            else:
                res[idx] = r_max - 1
                
        print(res)
        return sum(res)