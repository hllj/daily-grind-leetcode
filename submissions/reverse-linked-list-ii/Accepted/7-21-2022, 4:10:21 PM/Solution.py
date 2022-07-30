// https://leetcode.com/problems/reverse-linked-list-ii

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        p = head
        prev = None
        while left > 1:
            prev = p
            p = p.next
            left -= 1
            right -= 1
        
        tail, con = p, prev
        while right:
            third = p.next
            p.next = prev
            prev = p
            p = third
            right -= 1
        if con:
            con.next = prev
        else:
            head = prev
        tail.next = p
        return head