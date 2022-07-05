// https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        u = 0
        while u < len(nums):
            if nums[u] == 0:
                return False
            u += nums[u]
            print('u', u)
        if u >= len(nums):
            return True
        else:
            return False