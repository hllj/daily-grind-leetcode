// https://leetcode.com/problems/ways-to-split-array-into-three-subarrays

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        modulo = int(1e9 + 7)
        res = 0
        for i in range(0, n - 1):
            s1 = nums[i]
            l = i + 1
            r = n - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] - s1 >= s1:
                    s2 = nums[m] - s1
                    s3 = nums[n - 1] - nums[m - 1]
                    if (s1 <= s2 <= s3):
                        res += 1
                    r = m - 1
                else:
                    l = m + 1
        return res % modulo
        