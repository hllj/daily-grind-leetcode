// https://leetcode.com/problems/longest-increasing-subsequence

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        inf = 2501
        b = [inf] * (n + 1)
        b[0] = -inf
        res = 1
        for i in range(1, n + 1):
            l = 1
            r = n
            can = -1
            while l <= r:
                m = (l + r) // 2
                if b[m] >= nums[i - 1]:
                    can = m
                    r = m - 1
                else:
                    l = m + 1
            b[can] = nums[i - 1]
            print(can)
            res = max(res, can)
        print(b)
        return res