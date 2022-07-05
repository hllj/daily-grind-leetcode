// https://leetcode.com/problems/short-encoding-of-words

class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        words = set(words)
        remove_set = []
        for word in words:
            for k in range(1, len(word)):
                suffix = word[k:]
                if suffix in words:
                    remove_set.append(suffix)
        for s in remove_set:
            words.remove(s)
        res = 0
        for word in words:
            res += len(word) + 1
        return res