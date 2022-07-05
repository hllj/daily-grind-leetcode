// https://leetcode.com/problems/longest-common-prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = min([len(st) for st in strs])
        res = ""
        for i in range(1, min_len):
            pre = strs[0][:i]
            print(pre)
            flag = True
            for st in strs:
                if st[:i] != pre:
                    flag = False
                    break
            if (flag):
                res = pre
        return res