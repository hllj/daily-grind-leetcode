// https://leetcode.com/problems/apply-discount-to-prices

import re
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        sentence += ' '
        res = sentence
        print(re.findall("\s\$\d+(?:\.\d+)?", sentence))
        for match in finditer("\s\$\d+(?:\.\d+)?", sentence):
            pos_start = match.start()
            pos_end = match.end()
            print('start', 'end', pos_start, pos_end)
            x = sentence[pos_start:pos_end]
            m = x[1:]
            print('check', sentence[pos_end])
            if (sentence[pos_end] == '$'):
                continue
            new_m = round(float(m) - float(m) * discount / 100, 2)
            new_x = '$' + "{:.2f}".format(new_m)
            if sentence[pos_end - 1] == ' ':
                new_x += ' '
            res = res.replace(x, new_x)
        return res.strip()
        