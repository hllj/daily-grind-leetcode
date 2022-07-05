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
        mapping = {
            0: 0,
            1: 1,
            2: 1,
            3: 1,
            4: 2,
            5: 2,
        }
        for key in cnt:
            value = cnt[key]
            if value == 1:
                return -1
            d = value // 6
            c = value % 6
            res += 2 * d + mapping[c]
        return res