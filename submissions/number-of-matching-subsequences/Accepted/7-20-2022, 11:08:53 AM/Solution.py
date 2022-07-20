// https://leetcode.com/problems/number-of-matching-subsequences

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        words = sorted(words, key=lambda x: len(x))
        d = {}
        for word in words:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
        child = {}
        res = 0
        for word in d.keys():
            current = child
            i = 0
            j = 0
            for idx, c in enumerate(word):
                if c in current:
                    current = current[c]
                    i = idx
                    j = current['#']
                else:
                    break
            if word[i] == s[j]:
                i += 1
                j += 1
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
            if i == len(word):
                res += d[word]
        return res