// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        pos = {}
        pos[numbers[0]] = 0
        for i in range(1, len(numbers)):
            if (target - numbers[i]) in pos.keys():
                p = pos[target - numbers[i]]
                return [p + 1, i + 1]
            else:
                pos[numbers[i]] = i