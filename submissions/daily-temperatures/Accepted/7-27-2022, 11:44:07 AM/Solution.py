// https://leetcode.com/problems/daily-temperatures

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        n = len(temperatures)
        res = []
        for i in range(n - 1, -1 , -1):
            while len(st) > 0 and temperatures[st[-1]] <= temperatures[i]:
                st.pop(-1)
            if len(st) == 0:
                res.append(0)
            else:
                res.append(st[-1] - i)
            st.append(i)
        return res[::-1]