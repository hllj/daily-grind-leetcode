// https://leetcode.com/problems/design-add-and-search-words-data-structure

class WordDictionary:

    def __init__(self):
        self.child = {}

    def dfs(self, current, word, idx):
        if (idx == len(word)):
            return '#' in current
        if word[idx] == '.':
            check = False
            for i in range(ord('a'), ord('z') + 1):
                c = chr(i)
                t = current
                if c in t:
                    t = t[c]
                    check = check or self.dfs(t, word, idx + 1)
            return check
        else:
            if word[idx] not in current:
                return False
            current = current[word[idx]]
            return self.dfs(current, word, idx + 1)
                        
        
    def addWord(self, word: str) -> None:
        current = self.child
        for c in word:
            if c not in current:
                current[c] = {}
            current = current[c]
        current['#'] = 1

    def search(self, word: str) -> bool:
        current = self.child
        return self.dfs(current, word, 0)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)