// https://leetcode.com/problems/minimum-size-subarray-sum

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n + 1)
        res = int(1e5 + 1)
        for j in range(1, n + 1):
            f[j] = f[j - 1] + nums[j - 1]
            l = 1
            r = j
            while (l <= r):
                m = int((l + r) >> 1);
                if f[j] - f[m - 1] >= target:
                    res = min(res, j - m + 1)
                    l = m + 1
                else:
                    r = m - 1
        if res == int(1e5 + 1):
            return 0
        else:
            return res