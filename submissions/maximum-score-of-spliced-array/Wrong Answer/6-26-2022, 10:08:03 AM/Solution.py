// https://leetcode.com/problems/maximum-score-of-spliced-array

class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        if sum(nums2) < sum(nums1):
            nums1, nums2 = nums2, nums1
        n = len(nums1)
        sub = [0 for _ in range(n)]
        for i in range(n):
            sub[i] = nums1[i] - nums2[i]
        f = sub[0]
        res = f
        for i in range(1, n):
            f = max(sub[i], f + sub[i])
            res = max(res, f)
        if res < 0:
            return sum(nums2)
        else:
            return sum(nums2) + res