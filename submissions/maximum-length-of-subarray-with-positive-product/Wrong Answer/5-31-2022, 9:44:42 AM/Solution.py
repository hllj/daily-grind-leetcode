// https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                pos = 0
                reg = 0
            elif nums[i] > 0:
                pos += 1
                if neg != 0:
                    neg += 1
                res = max(res, pos)
            elif nums[i] < 0:
                pos, neg = neg, pos
                neg += 1
                if pos != 0:
                    pos += 1
                res = max(res, pos)
        return res
        