// https://leetcode.com/problems/top-k-frequent-elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for x in nums:
            if x not in d:
                d[x] = 1
            else:
                d[x] += 1
        d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)}
        return list(d.keys())[:k]