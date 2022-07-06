// https://leetcode.com/problems/length-of-longest-fibonacci-subsequence

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr)
        f = [0] * (n + 1)
        inf = int(1e3 + 1)
        b = [inf] * (n + 1)
        b[0] = -inf
        f[1] = 1
        res = 1
        for i in range(2, n + 1):
            for j in range(1, i):
                # l = 0
                # r = j - 1
                # v = arr[i - 1] - arr[j - 1]
                # while l <= r:
                #     m = (l + r) // 2
                #     if arr[m - 1] == v:
                #         f[i] = max(f[i], f[m] + 2)
                #         res = max(res, f[i])
                #         break
                #     if arr[m - 1] > v:
                #         r = m - 1
                #     else:
                #         l = m + 1
                for prev in range(1, j):
                    if arr[prev - 1] + arr[j - 1] == arr[i - 1]:
                        f[i] = max(f[i], f[prev] + 2)
                        res = max(res,  f[i])
        return res
    
# O(N^3) -> This one is fine

# O(N^2logN) -> Because "Given a strictly increasing array arr"
        
# f(i): longest length of fibonacci subseq end at i

# f(i) = f(prev) + 2 if a[prev] = a[i] - a[j] 
# res = max(res, f(i))