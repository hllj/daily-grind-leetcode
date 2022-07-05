// https://leetcode.com/problems/booking-concert-tickets-in-groups

class BookMyShow:

    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.row_status = [0] * n

    def gather(self, k: int, maxRow: int) -> List[int]:
        row_status_copy = self.row_status.copy()
        print('gather', k, maxRow)
        print('row status', row_status_copy)
        flag = False
        res = []
        for i in range(maxRow + 1):
            p = row_status_copy[i]
            print('p', p)
            print('condition', p + k, self.m)
            if (p + k <= self.m):
                row_status_copy[i] += k
                flag = True
                res = [i, p]
        if flag is True:
            self.row_status = row_status_copy
        return res

    def scatter(self, k: int, maxRow: int) -> bool:
        print('scatter', k, maxRow)
        row_status_copy = self.row_status.copy()
        for i in range(maxRow + 1):
            n_in = min(k, self.m - row_status_copy[i])
            k -= n_in
            row_status_copy[i] += n_in
        print('k scatter', k)
        if k == 0:
            self.row_status = row_status_copy
            return True
        else:
            return False


# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)