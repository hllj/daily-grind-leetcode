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
            r = -v - (s + v)
            heapq.heappushpop(target, -r)
            s = -v
            # print(target)
        for x in target:
            if x != -1:
                return False
        return True