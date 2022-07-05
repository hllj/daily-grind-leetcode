// https://leetcode.com/problems/partition-list

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less_root = None
        less_p = None
        greater_root = None
        greater_p = None
        p = head
        while p != None:
            if p.val < x:
                if less_root == None:
                    less_p = ListNode(p.val, None)
                    less_root = less_p
                else:
                    new_node = ListNode(p.val, None)
                    less_p.next = new_node
                    less_p = less_p.next
            else:
                if greater_root == None:
                    greater_p = ListNode(p.val, None)
                    greater_root = greater_p
                else:
                    new_node = ListNode(p.val, None)
                    greater_p.next = new_node
                    greater_p = greater_p.next
            p = p.next
        less_p.next = greater_root
        return less_root