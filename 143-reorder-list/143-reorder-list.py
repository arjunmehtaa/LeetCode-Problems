# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find middle
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
        # reverse 2nd half
        current = slow.next
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        slow.next = None
        
        # merge the two lists
        head1 = head
        head2 = prev
        final = ListNode()
        start = final
        while head1 and head2:
            final.next = head1
            head1 = head1.next
            final = final.next
            final.next = head2
            head2 = head2.next
            final = final.next
        final.next = head1 or head2
        
        return start.next
            
        
        
            
        