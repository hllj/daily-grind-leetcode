// https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts = sorted(horizontalCuts)
        horizontalCuts.insert(0, 0)
        horizontalCuts.append(h)
        verticalCuts = sorted(verticalCuts)
        verticalCuts.insert(0, 0)
        verticalCuts.append(w)
        max_h = 0
        for i in range(len(horizontalCuts) - 1):
            max_h = max(max_h, horizontalCuts[i + 1] - horizontalCuts[i])
        max_w = 0
        for i in range(len(verticalCuts) - 1):
            max_w = max(max_w, verticalCuts[i + 1] - verticalCuts[i])
        return (max_h * max_w) % (int(1e9) + 7)