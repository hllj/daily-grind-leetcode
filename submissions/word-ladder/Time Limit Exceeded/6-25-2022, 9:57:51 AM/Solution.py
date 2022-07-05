// https://leetcode.com/problems/word-ladder

class Solution:
    def check(self, x1, x2):
        cnt = 0
        for i in range(len(x1)):
            if cnt > 1:
                return False
            if x1[i] != x2[i]:
                cnt += 1
        if cnt == 1:
            return True
        return False
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        next_word = {}
        wordList.append(beginWord)
        # n = len(wordList)
        # for i in range(n):
        #     next_word[wordList[i]] = []
        #     for j in range(i + 1, n):
        #         if i != j and self.check(wordList[i], wordList[j]):
        #             next_word[wordList[i]].append(wordList[j])
        q = []
        q.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)
        while len(q) > 0:
            word, cnt = q.pop(0)
            for nxt in wordList:
                if nxt not in visited and self.check(word, nxt):
                    q.append((nxt, cnt + 1))
                    visited.add(nxt)
                    if nxt == endWord:
                        return cnt + 1
        return 0