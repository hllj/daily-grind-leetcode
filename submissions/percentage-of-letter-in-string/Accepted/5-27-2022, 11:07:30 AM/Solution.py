// https://leetcode.com/problems/percentage-of-letter-in-string

import math
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        cnt = s.count(letter)
        print(cnt / len(s))
        return int(math.floor(cnt / len(s) * 100))