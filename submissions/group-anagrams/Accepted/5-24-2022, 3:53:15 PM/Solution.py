// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for st in strs:
            sorted_st =  ''.join(sorted(st))
            if sorted_st not in group:
                group[sorted_st] = [st]
            else:
                group[sorted_st].append(st)
        res = []
        for encode in group:
            gr = group[encode]
            res.append(gr)
        return res