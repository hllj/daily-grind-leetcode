// https://leetcode.com/problems/maximum-number-of-removable-characters

class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        s = list(s)
        
        p = list(p)
        l = 0
        r = len(removable)
        res = 0
        while l <= r:
            m = (l + r) // 2
            s_tmp = s.copy()
            for idx in range(m):
                s_tmp[removable[idx]] = " "
            i = 0
            j = 0
            print(m, s_tmp, p)
            while (i < len(s_tmp) and j < len(p)):
                if s[i] == ' ':
                    i += 1
                else:
                    if s_tmp[i] == p[j]:
                        i += 1
                        j += 1
                    else:
                        i += 1
            print(i, j)
            if (j == len(p)):
                res = m
                l = m + 1
            else:
                r = m - 1
        return res