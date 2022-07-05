// https://leetcode.com/problems/my-calendar-i

class MyCalendar:

    def __init__(self):
        self.booked_list = []

    def book(self, start: int, end: int) -> bool:
        is_intersect = False
        for l, r in self.booked_list:
            if not (start >= r or end <= l):
                is_intersect = True
                break
        if is_intersect == False:
            self.booked_list.append((start, end))
            return True
        else:
            return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)