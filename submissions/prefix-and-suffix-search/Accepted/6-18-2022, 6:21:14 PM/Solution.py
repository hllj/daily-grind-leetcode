// https://leetcode.com/problems/prefix-and-suffix-search

from itertools import zip_longest

class WordFilter:

    def __init__(self, words: List[str]):
        self.child = {}
        for idx, word in enumerate(words):
            current = self.child
            current['#'] = idx
            for i, x in enumerate(word):
                tmp = current
                for c in word[i:]:
                    if (c, None) not in tmp:
                        tmp[(c, None)] = {}
                    tmp = tmp[(c, None)]
                    tmp['#'] = idx
                tmp = current
                for c in word[:-i or None][::-1]:
                    if (None, c) not in tmp:
                        tmp[(None, c)] = {}
                    tmp = tmp[(None, c)]
                    tmp['#'] = idx
                if (x, word[~i]) not in current:
                    current[(x, word[~i])] = {}
                current = current[(x, word[~i])]
                current['#'] = idx
        # print(self.child)

    def f(self, prefix: str, suffix: str) -> int:
        current = self.child
        for a, b in zip_longest(prefix, suffix[::-1]):
            if (a, b) not in current:
                return -1
            current = current[(a, b)]
        # print(current)
        return current['#']


# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)