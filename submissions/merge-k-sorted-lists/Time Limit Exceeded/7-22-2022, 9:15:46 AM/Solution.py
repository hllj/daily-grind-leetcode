// https://leetcode.com/problems/merge-k-sorted-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = None
        p = None
        while True:
            val = None
            choose = None
            for idx, l in enumerate(lists):
                if l != None:
                    if (val == None) or (l.val < val):
                        val = l.val
                        choose = idx
            if val == None:
                break
            if head == None:
                head = ListNode(val=val, next=None)
                p = head
            else:
                p.next = ListNode(val=val, next=None)
                p = p.next
            lists[choose] = lists[choose].next
        return head