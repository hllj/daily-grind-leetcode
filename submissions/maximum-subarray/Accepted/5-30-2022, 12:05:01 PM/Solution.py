// https://leetcode.com/problems/maximum-subarray

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        f = nums[0]
        res = f
        for i in range(1, len(nums)):
            f = max(nums[i], f + nums[i])
            res = max(res, f)
        return res