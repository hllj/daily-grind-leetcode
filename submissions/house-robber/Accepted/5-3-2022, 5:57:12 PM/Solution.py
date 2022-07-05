// https://leetcode.com/problems/house-robber

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if (n == 1):
            return nums[0]
        if (n == 2):
            return max(nums[0], nums[1])
        f0 = nums[0]
        f1 = max(nums[0], nums[1])
        for i in range(2, n):
            fa = max(f0 + nums[i], f1)
            f0 = f1
            f1 = fa
        return fa