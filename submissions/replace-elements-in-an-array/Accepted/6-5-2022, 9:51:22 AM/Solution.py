// https://leetcode.com/problems/replace-elements-in-an-array

class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        d = {}
        for i, v in enumerate(nums):
            d[v] = i
        for operation in operations:
            u, v = operation
            i = d[u]
            d.pop(u)
            d[v] = i
        res = [v for v, i in sorted(d.items(), key=lambda x: x[1])]
        return res