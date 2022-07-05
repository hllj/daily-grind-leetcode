// https://leetcode.com/problems/sort-array-by-parity

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            if num % 2 == 0:
                res.insert(0, num)
            else:
                res.append(num)
        return res