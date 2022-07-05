// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for st in strs:
            sorted_st =  ''.join(sorted(st))
            if sorted_st in group:
                group[sorted_st].append(st)
            else:
                group[sorted_st] = [st]
        return group.values()