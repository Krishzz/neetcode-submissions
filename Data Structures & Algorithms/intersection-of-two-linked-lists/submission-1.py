# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if not headA or not headB:
            return None
        a_node = headA
        b_node = headB
        while a_node!=b_node:
            a_node = a_node.next if a_node else headB
            b_node = b_node.next if b_node else headA
        return a_node