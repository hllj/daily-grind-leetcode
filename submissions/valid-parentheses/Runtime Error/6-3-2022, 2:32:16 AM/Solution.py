// https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if stack[-1] == match[c]:
                    stack.pop()
        return len(stack) == 0