// https://leetcode.com/problems/rearrange-characters-to-make-target-string

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        s_cnt = [0] * 26
        target_cnt = [0] * 26
        for c in s:
            i = ord(c) - ord('a')
            s_cnt[i] += 1
        for c in target:
            i = ord(c) - ord('a')
            target_cnt[i] += 1
        res = 1000
        for i in range(26):
            if target_cnt[i] != 0:
                print('check', chr(i + ord('a')), target_cnt[i], s_cnt[i])
                res = min(res, s_cnt[i] // target_cnt[i])
        print(res)
        return res