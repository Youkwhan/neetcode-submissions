# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        combined_list = lists[0]
        for idx in range(1, len(lists)):
            combined_list = self.mergeTwoLists(combined_list, lists[idx])
        return combined_list


    def mergeTwoLists(self, l1,l2):
        #always merge l2 on to l1 
        sentinel = ListNode(-1)
        curr = sentinel

        while l1 and l2:
            if l1.val < l2.val:
                curr.next = l1 
                l1 = l1.next 
            else:
                curr.next = l2 
                l2 = l2.next
            curr = curr.next
        
        curr.next = l1 or l2 

        return sentinel.next
