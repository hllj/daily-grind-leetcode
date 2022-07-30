// https://leetcode.com/problems/contains-duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for x in nums:
            if x not in s:
                s.add(x)
            else:
                return True
        return False