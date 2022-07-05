// https://leetcode.com/problems/3sum-closest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = int(1e8 + 10)
        ret = -1
        nums.sort()
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                l = j + 1
                r = n - 1
                while l <= r:
                    m = (l + r) // 2
                    sum3 = nums[i] + nums[j] + nums[m]
                    d = sum3 - target
                    if abs(d) < res:
                        res = abs(d)
                        ret = sum3
                    if d < 0:
                        l = m + 1
                    else:
                        r = m - 1
        return ret