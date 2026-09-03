# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        true : if cycle else false

        1. slow=fast=head
        2. move 1, 2
        3. cycle till we meet
        4. reset slow
        5. iterate by 1 steps
        5. next time we meet it is the inital cycle start

        edge case - 
        """
        slow, fast = head, head

        # since we are moving by steps of 2 fast.nexrt
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                # meaning there is a possible cycle
                slow = head
                # bcz not moving by 2 steps now just fast
                while fast != slow:
                    slow = slow.next
                    fast = fast.next
                return True
        return False

            