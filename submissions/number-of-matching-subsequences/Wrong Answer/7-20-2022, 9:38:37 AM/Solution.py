// https://leetcode.com/problems/number-of-matching-subsequences

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        words = sorted(words, key=lambda x: len(x))
        child = {}
        child['#'] = 0
        res = []
        for word in words:
            current = child
            i = 0
            j = 0
            for idx, c in enumerate(word):
                if c not in current:
                    i = idx
                    j = current['#']
                    break
                else:
                    current = current[c]
            # print('check', i, j)
            while (i < len(word) and j < len(s)):
                if word[i] == s[j]:
                    if word[i] not in current:
                        current[word[i]] = {}
                    current = current[word[i]]
                    current['#'] = j
                    i += 1
                    j += 1
                else:
                    j += 1
            # print('done', i, j)
            if i == len(word):
                res.append(word)
            # if isSubsequence(word, s):
            #     res.append(word)
        return len(res)