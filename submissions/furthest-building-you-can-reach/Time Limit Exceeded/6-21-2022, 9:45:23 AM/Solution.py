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
        for i in range(1, n):
            heapq.heappush(li, diff[i])
            s_ladders[i] = sum(heapq.nlargest(min(len(li), ladders), li))
        s = 0
        for i in range(1, n):
            s += diff[i]
            if s - s_ladders[i] > bricks:
                return i - 1
        return n - 1