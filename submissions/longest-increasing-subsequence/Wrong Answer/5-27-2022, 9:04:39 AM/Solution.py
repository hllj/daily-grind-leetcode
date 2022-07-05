// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        inf = 2501
        b = [inf] * (n + 1)
        b[0] = -inf
        res = 1
        for x in nums:
            l = 0
            r = n - 1
            can = -1
            while l <= r:
                m = (l + r) // 2
                if b[m] >= x:
                    can = m
                    r = m - 1
                else:
                    l = m + 1
            b[can] = x
            res = max(res, can)
        return res