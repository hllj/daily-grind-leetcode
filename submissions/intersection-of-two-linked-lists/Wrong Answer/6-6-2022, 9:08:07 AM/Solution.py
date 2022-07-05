// https://leetcode.com/problems/intersection-of-two-linked-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA
        while pA.next != None:
            pB = headB
            while pB.next != None:
                if pB.next == pA.next:
                    return pB.next
                else:
                    pB = pB.next
            pA = pA.next
        return None