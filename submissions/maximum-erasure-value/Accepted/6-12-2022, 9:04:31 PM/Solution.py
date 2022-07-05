// https://leetcode.com/problems/maximum-erasure-value

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        f = [0] * (n + 1)
        for i in range(1, n + 1):
            f[i] = f[i - 1] + nums[i - 1]
        d = {}
        i = 0
        j = -1
        res = 0
        # print(f)
        while i < n:
            if nums[i] in d:
                if d[nums[i]] > j:
                    j = d[nums[i]]
            d[nums[i]] = i
            # print(i, j)
            if j == -1:
                res = max(res, f[i + 1])
            else:
                res = max(res, f[i + 1] - f[j + 1])
            i += 1
        return res