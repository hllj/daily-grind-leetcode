// https://leetcode.com/problems/implement-magic-dictionary

class Trie:
    def __init__(self):
        self.child = {}
    def insert(self, word):
        cur = self.child
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['#'] = 1
    def search(self, word):
        cur = self.child
        for c in word:
            if c not in cur:
                return False
            cur = cur[c]
        return '#' in cur

class MagicDictionary:

    def __init__(self):
        self.trie = Trie()

    def buildDict(self, dictionary: List[str]) -> None:
        for word in dictionary:
            self.trie.insert(word)

    def search(self, searchWord: str) -> bool:
        for i in range(len(searchWord)):
            for c in range(ord('a'), ord('z') + 1):
                if chr(c) != searchWord[i]:
                    candidate = searchWord[:i] + chr(c) + searchWord[i + 1:]
                    is_search = self.trie.search(candidate)
                    # print(candidate, is_search)
                    if is_search is True:
                        return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)