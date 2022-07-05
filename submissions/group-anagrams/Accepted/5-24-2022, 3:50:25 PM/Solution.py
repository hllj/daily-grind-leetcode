// https://leetcode.com/problems/group-anagrams

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        for st in strs:
            cnt = {}
            for c in st:
                if c not in cnt:
                    cnt[c] = 1
                else:
                    cnt[c] += 1
            encode = ''
            for c in range(97, 123):
                n = 0 if chr(c) not in cnt else cnt[chr(c)]
                encode += chr(c) + str(n)
            if encode not in group:
                group[encode] = [st]
            else:
                group[encode].append(st)
        res = []
        for encode in group:
            gr = group[encode]
            res.append(gr)
        return res