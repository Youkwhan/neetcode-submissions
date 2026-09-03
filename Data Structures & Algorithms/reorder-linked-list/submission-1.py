# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        reorder linked list
        alternate start with start, then end

        get mid point
        list 1, list2 (reverse this one)

        merge
        """
        #we want to interweave 
        #if we start fast 1 ahead - the slow pointer will end 1 BEFORE the midpoint
        slow, fast = head, head.next

        #get the slow pointer to right before midpoint
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        

        #reverse the list 

        #slow is pointing to the start of next list 
        prev = None
        curr = slow.next

        #disconnect the two lists 
        slow.next = None


        while curr:
            temp = curr.next
            curr.next = prev
            prev,curr = curr, temp

        #prev is now the new start of the reversed linked list 



        first, second = head, prev
        #the second list will be longer
        while second:
            temp1 = first.next
            temp2 = second.next
            first.next = second
            second.next = temp1 

            first, second = temp1, temp2


