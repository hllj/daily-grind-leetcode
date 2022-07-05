// https://leetcode.com/problems/min-max-game

class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        while len(nums) != 1:
            n = len(nums)
            new_nums = []
            for i in range(0, n, 2):
                if (i / 2) % 2 == 0:
                    new_nums.append(min(nums[i], nums[i + 1]))
                else:
                    new_nums.append(max(nums[i], nums[i + 1]))
            nums = new_nums
        return nums[0]