// https://leetcode.com/problems/generate-parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        lo = 0
        hi = 1 << (2 * n)
        a = [0 for _ in range(2 * n)]
        res = []
        for st in range(lo, hi):
            cnt0 = 0
            cnt1 = 0
            stack = []
            for i in range(2 * n):
                a[i] = (st >> i) & 1
                if a[i] == 0:
                    stack.append(a[i])
                else:
                    if len(stack) > 0 and stack[-1] == 1 - a[i]:
                        stack.pop()
                    else:
                        stack.append(a[i])
            if len(stack) == 0:
                res.append(''.join(['(' if x == 0 else ')' for x in a]))
        return res