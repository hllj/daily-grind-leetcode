// https://leetcode.com/problems/combination-sum

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(v, li):
            if v == target:
                print(v, li)
                if sorted(li) not in res:
                    res.append(sorted(li))
            for x in candidates:
                if (v + x <= target):
                    li.append(x)
                    v += x
                    backtrack(v, li)
                    v -= x
                    li.pop()
        v = 0
        li = []
        backtrack(v, li)
        return res