// https://leetcode.com/problems/single-element-in-a-sorted-array

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if m % 2 == 0:
                idx = m + 1
            else:
                idx = m - 1
            if nums[m] == nums[idx]:
                l = m + 1
            else:
                r = m
        return nums[l]