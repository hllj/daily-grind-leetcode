// https://leetcode.com/problems/word-subsets

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def count(word):
            d = [0] * 26
            for i in range(26):
                d[i] = 0
            for x in word:
                d[ord(x) - ord('a')] += 1
            return d
        union_dict = [0] * 26
        for word in words2:
            count_dict = count(word)
            for i in range(26):
                union_dict[i] = max(union_dict[i], count_dict[i])
        res = []
        for word in words1:
            flag = True
            count_dict = count(word)
            for i in range(26):
                if count_dict[i] < union_dict[i]:
                    flag = False
                    break
            if flag:
                res.append(word)
        return res