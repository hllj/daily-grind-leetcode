// https://leetcode.com/problems/jump-game-vi

import heapq
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        f = []
        f.append((-nums[0], 0))
        for i in range(1, n):
            while True:
                t = f[0]
                if i - t[1] > k:
                    heapq.heappop(f)
                    continue
                else:
                    v = -t[0] + nums[i]
                    heapq.heappush(f, (-v, i))
                    if i == n - 1:
                        return v
                    break