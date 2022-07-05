// https://leetcode.com/problems/maximum-product-subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_prod = nums[0]
        min_prod = nums[0]
        res = nums[0]
        for i in range(1, len(nums)):
            tmp_max_prod = max_prod
            tmp_min_prod = min_prod
            max_prod = max(tmp_min_prod * nums[i], tmp_max_prod * nums[i], nums[i])
            min_prod = min(tmp_min_prod * nums[i], tmp_max_prod * nums[i], nums[i])
            res = max(res, max_prod, min_prod)
        return res