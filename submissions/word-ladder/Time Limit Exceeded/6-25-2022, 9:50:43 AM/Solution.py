// https://leetcode.com/problems/word-ladder

class Solution:
    def check(self, x1, x2):
        cnt = 0
        for i in range(len(x1)):
            if x1[i] != x2[i]:
                cnt += 1
        if cnt == 1:
            return True
        return False
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        next_word = {}
        wordList.append(beginWord)
        n = len(wordList)
        for i in range(n):
            next_word[wordList[i]] = []
            for j in range(n):
                if i != j and self.check(wordList[i], wordList[j]):
                    next_word[wordList[i]].append(wordList[j])
        # print(next_word)
        q = []
        q.append((beginWord, 1))
        visited = set()
        visited.add(beginWord)
        while len(q) > 0:
            word, cnt = q.pop(0)
            # print(word, cnt)
            for nxt in next_word[word]:
                if nxt not in visited:
                    q.append((nxt, cnt + 1))
                    visited.add(nxt)
                    # print('next', nxt, cnt + 1)
                    if nxt == endWord:
                        return cnt + 1
        return 0