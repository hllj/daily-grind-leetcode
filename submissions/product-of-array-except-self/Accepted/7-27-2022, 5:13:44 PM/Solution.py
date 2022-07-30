// https://leetcode.com/problems/product-of-array-except-self

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        n = len(nums)
        ans = [0] * n
        for i in range(n):
            ans[i] = p
            p *= nums[i]
        p = 1
        for i in range(n - 1, -1, -1):
            ans[i] *= p
            p *= nums[i]
        return ans