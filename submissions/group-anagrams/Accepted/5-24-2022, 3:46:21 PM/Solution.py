// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for st in strs:
            cnt = {}
            for c in range(97, 123):
                cnt[chr(c)] = 0
            for c in st:
                cnt[c] += 1
            encode = ''
            for c in range(97, 123):
                encode += chr(c) + str(cnt[chr(c)])
            if encode not in group:
                group[encode] = [st]
            else:
                group[encode].append(st)
        res = []
        for encode in group:
            gr = group[encode]
            res.append(gr)
        return res