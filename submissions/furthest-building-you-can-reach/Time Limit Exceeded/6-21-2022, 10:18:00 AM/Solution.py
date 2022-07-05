// https://leetcode.com/problems/furthest-building-you-can-reach

import heapq

class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n = len(heights)
        diff = [0] * n
        s_ladders = [0] * n
        for i in range(1, n):
            if heights[i] > heights[i - 1]:
                diff[i] = heights[i] - heights[i - 1]
            else:
                diff[i] = 0
        li = [diff[0]]
        heapq.heapify(li)
        sum_heap = 0
        for i in range(1, n):
            if diff[i] != 0:
                if len(li) < ladders:
                    heapq.heappush(li, diff[i])
                    sum_heap += diff[i]
                else:
                    if (ladders > 0) and (diff[i] > heapq.nsmallest(1, li)[0]):
                        min_ele = heapq.heappop(li)
                        heapq.heappush(li, diff[i])
                        sum_heap += diff[i] - min_ele
            s_ladders[i] = sum_heap
        s = 0
        res = 0
        for i in range(1, n):
            s += diff[i]
            if s - s_ladders[i] <= bricks:
                res = i
            else:
                break
        return res