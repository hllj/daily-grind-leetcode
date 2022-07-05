// https://leetcode.com/problems/count-subarrays-with-score-less-than-k

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l = 1
        s = nums[0]
        n = len(nums)
        f = [0 for _ in range(n + 1)]
        for i in range(n):
            f[i + 1] = f[i] + nums[i]
        i = 1
        j = 1
        cnt = 0
        while (j <= n):
            if (f[j] - f[i - 1]) * (j - i + 1) < k:
                cnt += (j - i + 1)
                j += 1
                while (i < j) and (j <= n) and (f[j] - f[i - 1]) * (j - i + 1) >= k:
                    i += 1
            else:
                i += 1
            
        return cnt