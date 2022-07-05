// https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return True
        u = n - 1
        for i in range(n - 2, -1, -1):
            if i + nums[i] >= u:
                u = i
        return u == 0