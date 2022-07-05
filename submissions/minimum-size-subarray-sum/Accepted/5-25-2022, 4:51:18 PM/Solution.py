// https://leetcode.com/problems/minimum-size-subarray-sum

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n + 1)
        f[0] = 0
        for i in range(1, n + 1):
            f[i] = f[i - 1] + nums[i - 1]
        if f[n] < target:
            return 0
        print(f)
        res = n
        for j in range(1, n + 1):
            l = 1
            r = j
            while (l <= r):
                m = int((l + r) >> 1);
                if f[j] - f[m - 1] >= target:
                    res = min(res, j - m + 1)
                    l = m + 1
                else:
                    r = m - 1
        return res