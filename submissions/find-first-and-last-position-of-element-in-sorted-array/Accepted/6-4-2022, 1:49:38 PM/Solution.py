// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        l = 0
        r = n - 1
        idx1 = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                idx1 = m
                r = m - 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        l = 0
        r = n - 1
        idx2 = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                idx2 = m
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
        if (idx1 == -1) or (nums[idx1] != target):
            return [-1, -1]
        return [idx1, idx2]
        