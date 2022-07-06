// https://leetcode.com/problems/length-of-longest-fibonacci-subsequence

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        d = {}
        for i in range(n):
            d[arr[i]] = i
        res = 2
        for i in range(n):
            for j in range(i + 1, n):
                l = 2
                a = arr[i]
                b = arr[j]
                while (a + b) in d and d[a + b] > j:
                    x = d[a + b]
                    l += 1
                    a = arr[j]
                    b = arr[x]
                res = max(res, l)
        return res