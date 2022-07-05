// https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l = min(bloomDay)
        r = max(bloomDay)
        res = -1
        while l <= r:
            mid = (l + r) // 2
            flower_cnt = 0
            bouquet = 0
            for x in bloomDay:
                if x <= mid:
                    flower_cnt += 1
                    if flower_cnt == k:
                        bouquet += 1
                        flower_cnt = 0
                else:
                    flower_cnt = 0
            if bouquet >= m:
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res