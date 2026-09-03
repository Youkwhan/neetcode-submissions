# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        output = ListNode(-1)
        curr = output
        #lets just use l1 as the return value 
        carry = 0 
        while l1 or l2 or carry:
            l1_val = l1.val if l1 else 0 
            l2_val = l2.val if l2 else 0 
            
            curr_sum = l1_val+l2_val+carry
            if curr_sum >= 10:
                curr_sum%=10
                carry = 1
            else:
                carry = 0 
            curr.next = ListNode(curr_sum)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next

        return output.next 