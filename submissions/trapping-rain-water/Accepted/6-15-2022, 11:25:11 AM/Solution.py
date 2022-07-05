// https://leetcode.com/problems/trapping-rain-water

class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        left = [0] * (n + 1)
        right = [0] * (n + 1)
        left[0] = height[0]
        for i in range(1, n):
            left[i] = max(left[i - 1], height[i])
        right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            right[i] = max(right[i + 1], height[i])
        res = 0
        for i in range(n):
            res += min(left[i], right[i]) - height[i]
        return res