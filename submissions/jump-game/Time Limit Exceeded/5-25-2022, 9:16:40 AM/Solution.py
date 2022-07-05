// https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        stack = [0]
        avail = {}
        avail[0] = True
        while len(stack) > 0:
            u = stack.pop(0)
            if u == n - 1:
                return True
            for i in range(1, nums[u] + 1):
                if (u + i) not in avail:
                    stack.append(u + i)
                    avail[u + i] = True
        return False