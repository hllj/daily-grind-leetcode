// https://leetcode.com/problems/search-suggestions-system

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        self.child = {}
        for product in products:
            current = self.child
            for c in product:
                if c not in current:
                    current[c] = {}
                current = current[c]
                if '#' not in current:
                    current['#'] = [product]
                else:
                    current['#'].append(product)
        current = self.child
        res = []
        for c in searchWord:
            if c not in current:
                res.append([])
                current[c] = {}
                current = current[c]
            else:
                current = current[c]
                list_product = sorted(current['#'])
                res.append(list_product[:3])
        return res