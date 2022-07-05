// https://leetcode.com/problems/house-robber-ii

class Solution:
    def calc(self, nums):
        n = len(nums)
        f0 = nums[0]
        f1 = max(nums[0], nums[1])
        for i in range(2, n):
            fa = max(f0 + nums[i], f1)
            f0 = f1
            f1 = fa
        return f1
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        return max(self.calc(nums[:-1]), self.calc(nums[1:]))