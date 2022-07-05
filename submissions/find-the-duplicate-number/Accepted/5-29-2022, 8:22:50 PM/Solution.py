// https://leetcode.com/problems/find-the-duplicate-number

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = [0] * (n + 1)
        for i in nums:
            cnt[i] += 1
            if cnt[i] == 2:
                return i