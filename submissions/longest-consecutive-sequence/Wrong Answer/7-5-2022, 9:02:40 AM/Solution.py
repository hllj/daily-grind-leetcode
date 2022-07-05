// https://leetcode.com/problems/longest-consecutive-sequence

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)
        lcs = 1
        cur = 1
        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                cur += 1
                lcs = max(lcs, cur)
            else:
                cur = 1
        return lcs