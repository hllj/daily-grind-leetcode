// https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt = {}
        for x in tasks:
            if x not in cnt:
                cnt[x] = 1
            else:
                cnt[x] += 1
        res = 0
        for key, value in cnt.items():
            if value < 2:
                return -1
            res += value // 3
            if (value % 3) % 2 == 0:
                res += (value % 3) // 2
            else:
                if (value % 2) == 0:
                    res += value // 2
                else:
                    d = value - ((value // 2) - 1) * 2
                    if d % 3 == 0:
                        res += d // 3
                    else:
                        return -1
        return res