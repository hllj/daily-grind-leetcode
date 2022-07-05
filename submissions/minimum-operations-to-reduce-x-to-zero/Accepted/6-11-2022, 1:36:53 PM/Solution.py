// https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        # left = [0] * (n + 1)
        right = [0] * (n + 1)
        # left[0] = 0
        # for i in range(1, n + 1):
            # left[i] = nums[i - 1] + left[i - 1]
        right[n] = 0
        for i in range(n - 1, -1, -1):
            right[i] = nums[i] + right[i + 1]
        res = None
        for i in range(0, n + 1):
            if i == 0:
                left_sum = 0
            else:
                left_sum += nums[i - 1]
            # left_sum = left[i]
            l = i
            r = n
            # print('left sum', left_sum)
            while l <= r:
                m = (l + r) // 2
                # print('check', m, left_sum + right[m])
                if right[m] == x - left_sum:
                    res = min(res, i + n - m) if res != None else i + n - m
                    break
                if right[m] > x - left_sum:
                    l = m + 1
                else:
                    r = m - 1
        if res == None:
            return -1
        return res