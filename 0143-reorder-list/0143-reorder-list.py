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
        if not head:
            return None
        
        # Find the middle
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        current = slow.next
        
        # Reverse second half
        prev = None
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        slow.next = None
        
        # Merge the two lists
        head1 = head
        head2 = prev
        while head2:
            temp1 = head1.next
            temp2 = head2.next
            head1.next = head2
            head2.next = temp1
            head1 = temp1
            head2 = temp2
        return head
    