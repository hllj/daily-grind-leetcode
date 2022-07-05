// https://leetcode.com/problems/my-calendar-i

class Node:
    def __init__(self, booked=False):
        self.booked = booked
        self.left = self.right = None

class MyCalendar:
    lo = 0
    hi = int(1e9)
    def __init__(self):
        self.root = None
        
    def search(self, root, start, end, lo, hi):
        if not root or start > end or start > hi or end < lo:
            return False
        if root.booked:    
            return True
        mid = (lo + hi) // 2
        left_search = self.search(root.left, start, end, lo, mid)
        right_search = self.search(root.right, start, end, mid + 1, hi)
        return left_search or right_search

    def insert(self, root, start, end, lo, hi):
        if start > end or start > hi or end < lo:
            return root
        if root == None:
            root = Node()
        if (start <= lo and hi <= end):
            root.booked = True
            return root
        mid = (lo + hi) // 2
        root.left = self.insert(root.left, start, end, lo, mid)
        root.right = self.insert(root.right, start, end, mid + 1, hi)
        root.booked = root.left and root.left.booked and root.right and root.right.booked
        return root
        

    def book(self, start: int, end: int) -> bool:
        is_found = self.search(self.root, start, end - 1, self.lo, self.hi)
        # print(is_found)
        if is_found == False:
            self.root = self.insert(self.root, start, end - 1, self.lo, self.hi)
            # print('insert', self.root)
            return True
        else:
            return False


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)