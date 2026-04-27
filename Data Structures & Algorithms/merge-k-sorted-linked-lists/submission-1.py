# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        for i in range(1,len(lists)):
            new_lst = ListNode('0')
            dummy = new_lst
            lst1 = lists[i-1]
            lst2 = lists[i]
            while lst1 and lst2:
                if lst1.val < lst2.val:
                    dummy.next = lst1
                    lst1 = lst1.next
                else:
                    dummy.next = lst2
                    lst2 = lst2.next
                dummy = dummy.next
            dummy.next = lst1 if lst1 else lst2 
            lists[i] = new_lst.next
        return lists[-1]
