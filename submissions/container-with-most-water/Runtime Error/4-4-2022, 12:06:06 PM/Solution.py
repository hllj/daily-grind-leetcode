// https://leetcode.com/problems/container-with-most-water

class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        res = 0
        while left <= right:
            res = max(res, min(height[left], height[right]) * (right - left))
            if height[left + 1] > height[left]:
                left += 1
            else:
                right -= 1
        return res
            