// https://leetcode.com/problems/valid-triangle-number

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(nums)
        res = 0
        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                upper = nums[j] + nums[i]
                l = j + 1
                r = n - 1
                upper_idx = -1
                while (l <= r):
                    m = (l + r) // 2
                    if nums[m] < upper:
                        upper_idx = m
                        l = m + 1
                    else:
                        r = m - 1
                if (upper_idx == -1):
                    continue
                res += (upper_idx - (j + 1) + 1)
        return res
                        