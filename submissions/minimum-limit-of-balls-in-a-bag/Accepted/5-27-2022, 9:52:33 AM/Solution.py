// https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        l = 1
        r = max(nums)
        res = 0
        while l <= r:
            m = (l + r) // 2
            n_ops = 0
            for x in nums:
                n_ops += (x - 1) // m
            if n_ops <= maxOperations:
                res = m
                r = m - 1
            else:
                l = m + 1
        return res