// https://leetcode.com/problems/delete-and-earn

class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        n = len(nums)
        m = int(1e4)
        cnt = [0] * (m + 1)
        f = [0] * (m + 1)
        for x in nums:
            cnt[x] += 1
        res = 0
        for i in range(1, m + 1):
            f[i] = max(f[i - 1], f[i - 2] + cnt[i] * i)
            res = max(res, f[i])
        return res
        
# f(i): maximum points when choosing num i
# f(i) = max(f[i - 1], f(i - 2) + cnt(i) * i)
# res = max(f(i), res)

# cnt[2] = 2, cnt[3] = 3, cnt[4] = 1
# f(i) = cnt[i] * i + f(i - 2)