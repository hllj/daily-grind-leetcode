// https://leetcode.com/problems/short-encoding-of-words

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)
        remove_s = set()
        for word in words:
            for k in range(1, len(word)):
                suffix = word[k:]
                if suffix in words:
                    remove_s.add(suffix)
        res = 0
        for word in words:
            if word not in remove_s:
                res += len(word) + 1
        return res