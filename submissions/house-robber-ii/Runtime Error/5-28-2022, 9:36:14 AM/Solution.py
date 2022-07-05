// https://leetcode.com/problems/house-robber-ii

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        f = [0 for i in range(n)]
        f[0] = nums[0]
        f[1] = max(nums[0], nums[1])
        for i in range(n - 1):
            f[i] = max(f[i - 2] + nums[i], f[i - 1])
        return max()