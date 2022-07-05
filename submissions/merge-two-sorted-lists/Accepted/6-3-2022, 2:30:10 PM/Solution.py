// https://leetcode.com/problems/merge-two-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        p = None
        while list1 != None or list2 != None:
            if list1 != None and list2 != None:
                min_value = min(list1.val, list2.val)
                if min_value == list1.val:
                    list1 = list1.next
                else:
                    list2 = list2.next
            else:
                if list1 == None:
                    min_value = list2.val
                    list2 = list2.next
                else:
                    min_value = list1.val
                    list1 = list1.next
            if head == None:
                head = ListNode(min_value, None)
                p = head
            else:
                p.next = ListNode(min_value, None)
                p = p.next
        return head