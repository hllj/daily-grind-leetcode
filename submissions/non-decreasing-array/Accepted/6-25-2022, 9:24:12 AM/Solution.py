// https://leetcode.com/problems/non-decreasing-array

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        inf = 1e5 + 1
        nums.insert(0, -inf)
        nums.append(inf)
        n = len(nums)
        pos = []
        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                pos.append(i)
        if len(pos) > 1:
            return False
        if len(pos) == 0:
            return True
        x = pos[0]
        if (nums[x - 1] <= nums[x] <= nums[x + 2]) or (nums[x - 1] <= nums[x + 1] <= nums[x + 2]):
            return True
        return False
        