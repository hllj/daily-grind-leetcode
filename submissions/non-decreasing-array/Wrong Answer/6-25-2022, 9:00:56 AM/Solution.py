// https://leetcode.com/problems/non-decreasing-array

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        pos = []
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                pos.append(i)
        if len(pos) > 1:
            return False
        return True