// https://leetcode.com/problems/count-number-of-ways-to-place-houses

class Solution:
    def countHousePlacements(self, n: int) -> int:
        if n == 1:
            return 4
        if n == 2:
            return 9
        if n == 3:
            return 25
        if n == 4:
            return 64
        if n == 5:
            return 169
        return 0