// https://leetcode.com/problems/maximum-bags-with-full-capacity-of-rocks

class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        n = len(capacity)
        for i in range(n):
            capacity[i] -= rocks[i]
        capacity.sort()
        res = 0
        for i in range(n):
            if additionalRocks >= capacity[i]:
                additionalRocks -= capacity[i]
                res += 1
            else:
                break
        return res