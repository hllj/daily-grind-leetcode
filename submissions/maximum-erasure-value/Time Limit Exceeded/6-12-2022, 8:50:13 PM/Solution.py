// https://leetcode.com/problems/maximum-erasure-value

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        for i in range(n):
            s = set()
            sum = 0
            for j in range(i, n):
                sum += nums[j]
                s.add(nums[j])
                # print(len(s), i, j)
                if len(s) == j - i + 1:
                    res = max(res, sum)
                else:
                    break
        return res