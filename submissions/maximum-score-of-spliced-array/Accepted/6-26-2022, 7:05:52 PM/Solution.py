// https://leetcode.com/problems/maximum-score-of-spliced-array

class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        sub1 = [0 for _ in range(n)]
        sub2 = [0 for _ in range(n)]
        for i in range(n):
            sub1[i] = nums1[i] - nums2[i]
            sub2[i] = nums2[i] - nums1[i]
        f1 = sub1[0]
        res1 = f1
        f2 = sub2[0]
        res2 = f2
        for i in range(1, n):
            f1 = max(sub1[i], f1 + sub1[i])
            res1 = max(res1, f1)
            f2 = max(sub2[i], f2 + sub2[i])
            res2 = max(res2, f2)
        # print('max sub array', res1)
        # print('max sub array', res2)
        if res1 < 0 and res2 < 0:
            return max(sum(nums1), sum(nums2))
        else:
            return max(sum(nums2) + res1, sum(nums1) + res2)