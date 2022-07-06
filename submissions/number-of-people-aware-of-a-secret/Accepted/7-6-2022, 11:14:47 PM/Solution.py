// https://leetcode.com/problems/number-of-people-aware-of-a-secret

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        f = [[0 for _ in range(forget)] for _ in range(n + 1)]
        f[1][0] = 1
        modulo = int(1e9 + 7)
        for i in range(2, n + 1):
            for j in range(forget):
                if j > 0:
                    f[i][j] = f[i - 1][j - 1]
                else:
                    f[i][j] = 0
                    for x in range(delay - 1, forget - 1):
                        f[i][j] = (f[i][j] + f[i - 1][x]) % modulo
        return sum(f[-1][:]) % modulo
        