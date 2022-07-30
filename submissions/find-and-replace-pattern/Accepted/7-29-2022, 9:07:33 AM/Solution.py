// https://leetcode.com/problems/find-and-replace-pattern

class Solution:
    def check(self, word, pattern):
        n = len(word)
        dw = {}
        dp = {}
        for i in range(n):
            if word[i] not in dw and pattern[i] not in dp:
                dw[word[i]] = pattern[i]
                dp[pattern[i]] = word[i]
            else:
                if (word[i] in dw and dw[word[i]] != pattern[i]) or (pattern[i] in dp and dp[pattern[i]] != word[i]):
                    return False
        # print('dict', dw, dp)
        return True
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        print(self.check('abc', 'abb'))
        res = []
        for word in words:
            if self.check(word, pattern):
                res.append(word)
        return res