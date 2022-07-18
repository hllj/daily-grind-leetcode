// https://leetcode.com/problems/subarray-sum-equals-k

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        pref = 0
        d = {0: 1}
        res = 0
        for num in nums:
            pref += num
            if pref - k in d:
                res += d[pref - k]
            if pref not in d:
                d[pref] = 1
            else:
                d[pref] += 1
        return res