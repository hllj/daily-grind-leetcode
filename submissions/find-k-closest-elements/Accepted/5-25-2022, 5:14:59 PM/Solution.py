// https://leetcode.com/problems/find-k-closest-elements

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        l = []
        for i in range(n):
            l.append({
                'dis': abs(arr[i] - x),
                'v': arr[i],
                'index': i
            })
        l = sorted(l, key=lambda x: (x['dis'], x['v']))
        res = []
        for i in range(k):
            res.append(l[i]['v'])
        res = sorted(res)
        return res