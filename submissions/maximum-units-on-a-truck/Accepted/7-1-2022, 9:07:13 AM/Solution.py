// https://leetcode.com/problems/maximum-units-on-a-truck

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        n = len(boxTypes)
        res = 0
        s = 0
        for i in range(n):
            if s + boxTypes[i][0] <= truckSize:
                s += boxTypes[i][0]
                res += boxTypes[i][0] * boxTypes[i][1]
            else:
                res += max(0, truckSize - s) * boxTypes[i][1]
                break
        return res