// https://leetcode.com/problems/running-sum-of-1d-array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningSum = []
        s = 0
        for x in nums:
            s += x
            runningSum.append(s)
        return runningSum