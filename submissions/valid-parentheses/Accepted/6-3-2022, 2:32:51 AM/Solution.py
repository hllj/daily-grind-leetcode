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
                if len(stack) > 0 and stack[-1] == match[c]:
                    stack.pop()
                else:
                    stack.append(c)
        return len(stack) == 0