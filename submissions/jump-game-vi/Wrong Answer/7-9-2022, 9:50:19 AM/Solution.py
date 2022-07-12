// https://leetcode.com/problems/jump-game-vi

import heapq
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        n = len(nums)
        f = []
        f.append((-nums[0], 0))
        # f[0] = nums[0]
        for i in range(1, n):
            v = -float('inf')
            # for t in range(1, k + 1):
            #     if i - t >= 0:
            #         # print(i - t, f[i - t], nums[i - t])
            #         f[i] = max(f[i], f[i - t] + nums[i])
            # print(i, f[i])
            while True:
                t = f[0]
                if i - t[1] > k:
                    heapq.heappop(f)
                    continue
                else:
                    v = max(v, -t[0] + nums[i])
                    # print(i, v)
                    heapq.heappush(f, (-v, i))
                    if i == n - 1:
                        return v
                    break