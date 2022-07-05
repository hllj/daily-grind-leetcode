// https://leetcode.com/problems/subarray-product-less-than-k

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        p = 1
        cnt = 0
        i = 0
        for j in range(len(nums)):
            p *= nums[j]
            while p >= k:
                p //= nums[i]
                i += 1
            cnt += j - i + 1
        return cnt