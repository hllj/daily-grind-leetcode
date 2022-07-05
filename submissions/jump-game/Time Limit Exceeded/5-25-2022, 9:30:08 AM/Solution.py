// https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp = [False] * len(nums)
        dp[0] = True
        for u in range(0, len(nums)):
            if dp[u] == True:
                for i in range(1, nums[u] + 1):
                    if (u + i < len(nums)):
                        dp[u + i] = True
                    else:
                        break
            else:
                continue
        return dp[len(nums) - 1]