// https://leetcode.com/problems/frequency-of-the-most-frequent-element

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        n = len(nums)
        s = [0] * n
        for i in range(0, n):
            s[i] = s[i - 1] + nums[i]
        res = 1
        for i in range(n):
            # inc = k
            # fre = 1
            # for j in range(i - 1, -1, -1):
            #     if (inc >= 0) and (nums[j] + inc >= nums[i]):
            #         inc -= nums[i] - nums[j]
            #         fre += 1
            #     else:
            #         break
            # res = max(res, fre)
            l = 0
            r = i - 1
            idx = -1
            while l <= r:
                m = (l + r) // 2
                s1 = s[i-1]
                if m != 0:
                    s1 -= s[m - 1]
                if k >= (i - m) * nums[i] - s1:
                    idx = m
                    r = m - 1
                else:
                    l = m + 1
            if idx != -1:
                res = max(res, 1 + i - idx)
        return res
    
# s = [0, 1, 3, 7]