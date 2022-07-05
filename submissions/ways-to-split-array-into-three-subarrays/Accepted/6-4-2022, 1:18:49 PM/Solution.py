// https://leetcode.com/problems/ways-to-split-array-into-three-subarrays

class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(1, n):
            nums[i] += nums[i - 1]
        modulo = int(1e9 + 7)
        res = 0
        for i in range(n - 1):
            s1 = nums[i]
            if s1 > (nums[n - 1] - s1) / 2:
                break
            l = i + 1
            r = n - 2
            idx1 = -1
            while (l <= r):
                m = (l + r) // 2
                s2 = nums[m] - nums[i]
                s3 = nums[n - 1] - nums[m]
                if s1 <= s2 <= s3:
                    idx1 = m
                    r = m - 1
                elif s1 > s2:
                    l = m + 1
                else:
                    r = m - 1
            l = i + 1
            r = n - 2
            idx2 = -1
            while (l <= r):
                m = (l + r) // 2
                s2 = nums[m] - nums[i]
                s3 = nums[n - 1] - nums[m]
                if s1 <= s2 <= s3:
                    idx2 = m
                    l = m + 1
                elif (s1 > s2):
                    l = m + 1
                else:
                    r = m - 1
            if (idx1 == -1) or (idx2 == -1):
                continue
            res += (idx2 - idx1 + 1)
                
        return res % modulo
        