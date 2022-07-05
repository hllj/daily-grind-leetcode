// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n + 1)
        f[0] = nums[0]
        res = f[0]
        for i in range(1, n):
            f[i] = max(nums[i], f[i - 1] + nums[i])
            res = max(res, f[i])
        return res