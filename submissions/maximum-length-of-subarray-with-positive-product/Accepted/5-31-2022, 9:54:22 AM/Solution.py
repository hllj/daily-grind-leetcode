// https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        pos = 0
        neg = 0
        res = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                pos += 1
                if neg > 0:
                    neg += 1
            elif nums[i] < 0:
                tp = pos
                if neg > 0:
                    pos = neg + 1
                else:
                    pos = 0
                neg = tp + 1
            else:
                pos = neg = 0
            res = max(res, pos)
        return res
        