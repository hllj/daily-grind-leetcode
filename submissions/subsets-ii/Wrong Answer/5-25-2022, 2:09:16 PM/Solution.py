// https://leetcode.com/problems/subsets-ii

import itertools

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(0, n + 1):
            for c in itertools.combinations(nums, i):
                if list(c) not in res:
                    res.append(list(c))
        return res