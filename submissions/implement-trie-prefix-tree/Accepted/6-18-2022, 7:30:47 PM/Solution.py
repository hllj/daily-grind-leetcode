// https://leetcode.com/problems/implement-trie-prefix-tree

class Trie:

    def __init__(self):
        self.child = {}

    def insert(self, word: str) -> None:
        current = self.child
        for c in word:
            if c not in current:
                current[c] = {}
            current = current[c]
        current['#'] = 1

    def search(self, word: str) -> bool:
        current = self.child
        for c in word:
            if c not in current:
                return False
            current = current[c]
        return '#' in current

    def startsWith(self, prefix: str) -> bool:
        current = self.child 
        for c in prefix:
            if c not in current:
                return False
            current = current[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)