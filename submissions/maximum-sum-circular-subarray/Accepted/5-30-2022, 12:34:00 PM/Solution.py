// https://leetcode.com/problems/maximum-sum-circular-subarray

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        max_sub = nums[0]
        cur_max = nums[0]
        min_sub = nums[0]
        cur_min = nums[0]
        s = nums[0]
        for i in range(1, len(nums)):
            cur_max = max(nums[i], cur_max + nums[i])
            max_sub = max(max_sub, cur_max)
            cur_min = min(nums[i], cur_min + nums[i])
            min_sub = min(min_sub, cur_min)
            s += nums[i]
        if max_sub < 0:
            return max_sub
        else:
            return max(max_sub, s - min_sub)
        
# maximum subarray (i, j) with 0 <= i <= j < n -> Just using Kanade algorithm to solve

# maximum subarray (i, n - 1) + (0, j) with 0 <= i < n and 0 <= j, j < i