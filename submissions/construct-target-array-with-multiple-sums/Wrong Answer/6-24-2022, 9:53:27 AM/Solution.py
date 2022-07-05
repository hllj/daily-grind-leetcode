// https://leetcode.com/problems/construct-target-array-with-multiple-sums

import heapq
class Solution:
    def isPossible(self, target: List[int]) -> bool:
        s = sum(target)
        n = len(target)
        for i in range(n):
            target[i] *= -1
        heapq.heapify(target)
        while s > n:
            v = target[0]
            if -v - (s + v) <= 0:
                break
            n = -v // (s + v)
            r = -v - n * (s + v)
            if r < 1:
                r += (s + v)
            # r = -v - (s + v)
            heapq.heappushpop(target, -r)
            s = s + v + r
            # print(s)
            # print(target)
        print(target)
        for x in target:
            if x != -1:
                return False
        return True