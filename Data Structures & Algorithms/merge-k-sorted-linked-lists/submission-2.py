# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        while len(lists)>1:
            merged = []
            for i in range(0, len(lists), 2):
                lst1 = lists[i]
                lst2 = lists[i+1] if i+1<len(lists) else None
                merged.append(self.mergeLists(lst1, lst2))
            lists = merged
        return lists[-1]
    
    def mergeLists(self, lst1, lst2):
        dummy = ListNode('0')
        tail = dummy
        while lst1 and lst2:
            if lst1.val<lst2.val:
                tail.next = lst1
                lst1 = lst1.next
            else:
                tail.next = lst2
                lst2 = lst2.next
            tail = tail.next
        tail.next = lst1 or lst2
        return dummy.next
