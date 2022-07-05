// https://leetcode.com/problems/frequency-of-the-most-frequent-element

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        res = 1
        for i in range(n):
            inc = k
            fre = 1
            for j in range(i - 1, -1, -1):
                if (inc >= 0) and (nums[j] + inc >= nums[i]):
                    inc -= nums[i] - nums[j]
                    fre += 1
                else:
                    break
            res = max(res, fre)
        return res