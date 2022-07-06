// https://leetcode.com/problems/length-of-longest-fibonacci-subsequence

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        d = {}
        for i in range(n):
            d[arr[i]] = i
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                tmp_i = i
                tmp_j = j
                l = 2
                while (arr[tmp_i] + arr[tmp_j]) in d:
                    x = d[arr[tmp_i] + arr[tmp_j]]
                    tmp_i = tmp_j
                    tmp_j = x
                    l += 1
                if l > 2:
                    res = max(res, l)
        return res