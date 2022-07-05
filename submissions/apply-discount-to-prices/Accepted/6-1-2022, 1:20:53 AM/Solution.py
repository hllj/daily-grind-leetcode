// https://leetcode.com/problems/apply-discount-to-prices

import re
class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        word_split = sentence.split(' ')
        new_word = []
        for word in word_split:
            try:
                if word[0] == '$' and len(word) > 1:
                    m = 0
                    for c in word[1:]:
                        m = m * 10 + int(c)
                    new_m = "$" +  '{0:.2f}'.format(float(m) * (100 - discount) / 100)
                    new_word.append(new_m)
                else:
                    new_word.append(word)
            except:
                new_word.append(word)
        new_sentence = ' '.join(new_word)
        return new_sentence
        