// https://leetcode.com/problems/check-if-number-has-equal-digit-count-and-digit-value

class Solution:
    def digitCount(self, num: str) -> bool:
        n = len(num)
        d = [0] * n
        cnt = [0] * n
        for idx, c in enumerate(num):
            i = int(c)
            if not (0 <= i < n):
                return False
            cnt[i] += 1
            d[idx] = i
        print(d, cnt)
        return cnt == d
        