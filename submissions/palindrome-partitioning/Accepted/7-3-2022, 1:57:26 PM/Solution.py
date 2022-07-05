// https://leetcode.com/problems/palindrome-partitioning

class Solution:
    def check_palindrome(self, s):
        n = len(s)
        for i in range(n // 2):
            if s[i] != s[n - i - 1]:
                return False
        return True
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        f = [None for _ in range(n + 1)]
        f[0] = [['']]
        for i in range(1, n + 1):
            f[i] = []
            for j in range(i):
                if self.check_palindrome(s[j: i]):
                    # print('part', s[j: i])
                    for x in f[j]:
                        f[i].append(x + [s[j: i]])
            print(i, f[i])
        res = []
        for part in f[n]:
            part.remove('')
            res.append(part)
        return res