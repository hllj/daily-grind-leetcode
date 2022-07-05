// https://leetcode.com/problems/intersection-of-two-linked-lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        pA = headA
        pB = headB
        s = set()
        while pA != None:
            s.add(pA)
            pA = pA.next
        while pB != None:
            if pB in s:
                return pB
            s.add(pB)
            pB = pB.next
        return None