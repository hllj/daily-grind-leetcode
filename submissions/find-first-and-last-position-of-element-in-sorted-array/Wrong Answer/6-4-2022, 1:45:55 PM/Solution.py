// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l = 0
        r = n - 1
        idx1 = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] >= target:
                idx1 = m
                r = m - 1
            else:
                l = m + 1
        l = 0
        r = n - 1
        idx2 = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                idx2 = m
                r = m - 1
            else:
                l = m + 1
        if (idx1 == -1):
            return [-1, -1]
        while idx1 - 1 >= 0 and nums[idx1] > target:
            idx1 -= 1
        while idx2 - 1 >= 0 and nums[idx2] > target:
            idx2 -= 1
        if (nums[idx1] == target) and (nums[idx2] == target):
            return [idx1, idx2]
        else:
            return [-1, -1]