// https://leetcode.com/problems/add-two-numbers

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head_node = ListNode((l1.val + l2.val) % 10, None)
        p = head_node
        remainder = (l1.val + l2.val) // 10
        l1 = l1.next
        l2 = l2.next
        print(p.val, remainder)
        while (l1 != None or l2 != None):
            sum = 0
            if l1 != None:
                sum += l1.val
            if l2 != None:
                sum += l2.val
            sum += remainder
            next_node = ListNode(0, None)
            next_node.val = sum % 10
            remainder = sum // 10
            p.next = next_node
            p = next_node
            print(p.val, remainder)
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next
        if (remainder > 0):
            next_node = ListNode(remainder, None)
            p.next=  next_node
        return head_node
            