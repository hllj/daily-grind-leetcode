// https://leetcode.com/problems/steps-to-make-array-non-decreasing

class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        n = len(nums)
        st = []
        cnt = 0
        res = 0
        for idx, x in enumerate(nums):
            if len(st) > 0:
                if st[-1] > x:
                    print('stack', st)
                    print('remove', idx, x)
                    cnt += 1
                    print('cnt', cnt)
                else:
                    st.append(x)
                    print('add', cnt)
                    res = max(res, cnt)
                    cnt = 0
            else:
                st.append(x)
        print('stack last', st)
        return res