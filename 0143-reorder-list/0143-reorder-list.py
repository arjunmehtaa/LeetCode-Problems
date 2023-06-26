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
        # split list in 2
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        start = slow.next
        slow.next = None
        
        # reverse 2nd list
        prev = None
        current = start
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        
        # merge lists
        head1 = head
        head2 = prev
        ans = ListNode()
        ref = ans
        while head1 and head2:
            ans.next = head1
            head1 = head1.next
            ans = ans.next
            ans.next = head2
            head2 = head2.next
            ans = ans.next
        ans.next = head1 or head2
        
        return ans.next
        
        
        
        