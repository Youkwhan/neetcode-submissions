# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sentinel = ListNode(-1, head)
        group_prev = sentinel 

        while True:
            kth = self.get_kth(group_prev, k)
            if not kth:
                break 
            group_next = kth.next

            prev, curr = group_next ,group_prev.next
            while curr != group_next:
                temp = curr.next 
                curr.next = prev 
                prev, curr = curr, temp 
            #get the new "tail" aka start of previous group
            #link the group previous to the new "head"
            #kth is the old "tail" and new "head"
            new_tail = group_prev.next
            #link the previous with the new "head"
            group_prev.next = kth
            #reset, and previous group is the new "tail"
            group_prev = new_tail
        return sentinel.next


    def get_kth(self, node, k):
        while node and k > 0:
            node = node.next
            k -=1
        return node