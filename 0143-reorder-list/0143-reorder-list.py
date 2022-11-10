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
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        start = slow.next
        
        prev = None
        while start:
            next = start.next
            start.next = prev
            prev = start
            start = next
        slow.next = None
            
        current = head
        final = ListNode()
        p = final
        while current and prev:
            final.next = current
            final = final.next
            current = current.next
            final.next = prev
            final = final.next
            prev = prev.next
        final.next = current or prev
        
        return p.next
            