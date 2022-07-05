// https://leetcode.com/problems/longest-string-chain

class Solution:
    def is_predecessor(self, word1, word2):
        n1 = len(word1)
        n2 = len(word2)
        for i in range(n2):
            can_word = word2[:i] + word2[i + 1:]
            if can_word == word1:
                return True
        return False
    def longestStrChain(self, words: List[str]) -> int:
        words = sorted(words, key=lambda x: len(x))
        n = len(words)
        f = [0 for _ in range(n + 1)]
        f[0] = 1
        res = 1
        for i in range(1, n):
            f[i] = 1
            for j in range(0, i):
                if len(words[j]) == len(words[i]) - 1:
                    if self.is_predecessor(words[j], words[i]) is True:
                        f[i] = max(f[i], f[j] + 1)
            res = max(res, f[i])
        return res