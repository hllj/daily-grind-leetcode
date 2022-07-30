// https://leetcode.com/problems/reverse-linked-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = head
        prev = None
        while p != None:
            nxt = p.next
            p.next = prev
            prev = p
            if nxt == None:
                head = p
                break
            p = nxt
        return head