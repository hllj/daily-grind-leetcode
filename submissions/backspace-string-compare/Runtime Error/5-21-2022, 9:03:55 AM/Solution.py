// https://leetcode.com/problems/backspace-string-compare

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        new_s = []
        for i in range(len(s)):
            if s[i] == '#':
                new_s.pop()
            else:
                new_s.append(s[i])
            print(new_s)
        new_t = []
        for i in range(len(t)):
            if t[i] == '#':
                new_t.pop()
            else:
                new_t.append(t[i])
            print(new_t)
        print(new_s, new_t)
        return new_s == new_t