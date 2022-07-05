// https://leetcode.com/problems/minimum-absolute-sum-difference

class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        a = nums1.copy()
        a = sorted(a)
        n = len(nums1)
        sum_abs = 0
        for i in range(n):
            sum_abs += abs(nums1[i] - nums2[i])
        res = sum_abs
        for i in range(n):
            can_abs = sum_abs - abs(nums1[i] - nums2[i])
            l = 0
            r = n - 1
            idx = -1
            while l <= r:
                m = (l + r) // 2
                if a[m] < nums2[i]:
                    l = m + 1
                elif a[m] > nums2[i]:
                    r = m - 1
                elif a[m] == nums2[i]:
                    idx = m
                    break
                if idx != -1 and abs(a[m] - nums2[i]) < abs(a[idx] - nums2[i]):
                    idx = m
            if idx != -1:
                res = min(res, can_abs + abs(a[idx] - nums2[i]))
            else:
                for j in range(r, l + 1):
                    res = min(res, can_abs + abs(a[j] - nums2[i]))
        return res