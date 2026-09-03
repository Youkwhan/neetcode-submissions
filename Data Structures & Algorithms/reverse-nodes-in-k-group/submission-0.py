# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


  #so we have a chunk

  #prev of the reversed group. 
    #reverse the chunk in between
        #1.) iterate over k times 
        #2.) find where Next of group will be 
        #3.) reverse the list from group Prev to group Next
  #next of the reversed group

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        sentinel = ListNode(-1, head)
        group_prev = sentinel
        
        while True:
            kth = self.getKth(group_prev,k)
            #once we hit the end of the linkedlist
            if not kth:
                break
            group_next = kth.next

            #prev pointer part is confusing
            prev, curr = group_next , group_prev.next 
            while curr != group_next:
                temp = curr.next 
                curr.next= prev
                prev, curr = curr, temp 
            
            #so now

            temp = group_prev.next 
            group_prev.next = kth
            group_prev = temp
        return sentinel.next

    
    def getKth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k-=1
        return curr 