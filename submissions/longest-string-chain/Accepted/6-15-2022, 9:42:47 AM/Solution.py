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
        # Solution -> O((n * m)^2): n = len(words), m = max words len
        # words = sorted(words, key=lambda x: len(x))
        # n = len(words)
        # f = [0 for _ in range(n + 1)]
        # f[0] = 1
        # res = 1
        # for i in range(1, n):
        #     f[i] = 1
        #     for j in range(0, i):
        #         if len(words[j]) == len(words[i]) - 1:
        #             if self.is_predecessor(words[j], words[i]) is True:
        #                 f[i] = max(f[i], f[j] + 1)
        #     res = max(res, f[i])
        # return res
        
        words = sorted(words, key=lambda x: len(x))
        n = len(words)
        f = {}
        f[words[0]] = 1
        res = 1
        for i in range(1, n):
            max_len = 1
            for j in range(len(words[i])):
                pre = words[i][:j] + words[i][j + 1:]
                if pre in f:
                    max_len = max(max_len, f[pre] + 1)
            f[words[i]] = max_len
            res = max(res, max_len)
        return res