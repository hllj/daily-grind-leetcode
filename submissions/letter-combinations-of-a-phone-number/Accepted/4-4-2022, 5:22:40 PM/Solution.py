// https://leetcode.com/problems/letter-combinations-of-a-phone-number

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = ['']
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        for d in digits:
            tmp_res = []
            for c in letters[d]:
                for v in res:
                    tmp_res.append(v + c)
            res = tmp_res
        if res[0] == '':
            res = []
        return res