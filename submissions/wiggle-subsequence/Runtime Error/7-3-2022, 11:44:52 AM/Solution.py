// https://leetcode.com/problems/wiggle-subsequence

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        f = [[0, 0] for _ in range(n)]
        f[0][0] = 1
        f[0][1] = 1
        f[1][0] = 2 if nums[1] > nums[0] else 1
        f[1][1] = 2 if nums[1] < nums[0] else 1
        for i in range(2, n):
            f[i][0] = f[i - 1][0]
            f[i][1] = f[i - 1][1]
            for j in range(i):
                if nums[i] > nums[j]:
                    f[i][0] = max(f[i][0], f[j][1] + 1)
                if nums[j] > nums[i]:
                    f[i][1] = max(f[i][1], f[j][0] + 1)
        res = 1
        for i in range(n):
            res = max(res, f[i][0], f[i][1])
        return res
        