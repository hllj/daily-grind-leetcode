// https://leetcode.com/problems/booking-concert-tickets-in-groups

class BookMyShow:

    def __init__(self, n: int, m: int):
        self.n = n
        self.m = m
        self.row_status = [0] * n

    def gather(self, k: int, maxRow: int) -> List[int]:
        for i in range(maxRow + 1):
            p = self.row_status[i]
            if (p + k < self.m):
                self.row_status[i] += k
                return [i, p]
        return []

    def scatter(self, k: int, maxRow: int) -> bool:
        row_status_copy = self.row_status.copy()
        for i in range(maxRow + 1):
            n_in = min(k, self.m - row_status_copy[i])
            k -= n_in
            row_status_copy[i] += n_in
        if k == 0:
            return True
        else:
            return False


# Your BookMyShow object will be instantiated and called as such:
# obj = BookMyShow(n, m)
# param_1 = obj.gather(k,maxRow)
# param_2 = obj.scatter(k,maxRow)