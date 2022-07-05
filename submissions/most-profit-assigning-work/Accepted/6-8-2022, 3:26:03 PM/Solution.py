// https://leetcode.com/problems/most-profit-assigning-work

class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        job = []
        n = len(difficulty)
        for i in range(n):
            job.append((difficulty[i], profit[i]))
        job = sorted(job, key=lambda x: (x[0], x[1]))
        max_profit = [0] * n
        max_profit[0] = job[0][1]
        for i in range(1, n):
            max_profit[i] = max(max_profit[i - 1], job[i][1])
        # print(job)
        res = 0
        for x in worker:
            l = 0
            r = n - 1
            idx = -1
            while l <= r:
                m = (l + r) // 2
                if job[m][0] <= x:
                    idx = m
                    l = m + 1
                else:
                    r = m - 1
            if idx != -1:
                # print(x, max_profit[idx])
                res += max_profit[idx]
        return res