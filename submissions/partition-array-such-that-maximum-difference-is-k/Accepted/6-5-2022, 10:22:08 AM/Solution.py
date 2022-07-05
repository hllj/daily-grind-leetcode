// https://leetcode.com/problems/partition-array-such-that-maximum-difference-is-k

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums = sorted(nums, reverse=True)
        count = 0
        can = nums[0]
        for i in range(1, len(nums)):
            if can - nums[i] > k:
                count += 1
                can = nums[i]
        count += 1
        return count