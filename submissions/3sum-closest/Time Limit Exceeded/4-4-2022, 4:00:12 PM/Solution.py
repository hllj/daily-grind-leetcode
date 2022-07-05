// https://leetcode.com/problems/3sum-closest

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = int(1e8 + 10)
        ret = -1
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                sum2 = nums[i] + nums[j]
                x = target - sum2
                tmp = [nums[idx] for idx in range(n) if idx not in [i, j]]
                abs_tmp = [abs(v - x) for v in tmp]
                k = abs_tmp.index(min(abs_tmp))
                print(i, j, sum2, tmp[k], sum2 + tmp[k])
                if abs(target - (sum2 + tmp[k])) < res:
                    res = abs(target - (sum2 + tmp[k]))
                    ret = sum2 + tmp[k]
        return ret