// https://leetcode.com/problems/find-peak-element

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        inf = float('inf')
        for i in range(len(nums)):
            l = nums[i - 1] if i - 1 >= 0 else -inf
            r = nums[i + 1] if i + 1 < len(nums) else -inf
            if (nums[i] > l) and (nums[i] > r):
                return i
            