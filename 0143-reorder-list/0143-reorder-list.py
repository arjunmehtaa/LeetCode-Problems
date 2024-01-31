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
        slow.next = None
        
        prev = None
        while start:
            next = start.next
            start.next = prev
            prev = start
            start = next
            
        final = ListNode()
        p = final
        current = head
        while current and prev:
            p.next = current
            current = current.next
            p = p.next
            p.next = prev
            prev = prev.next
            p = p.next
        p.next = current or prev
        return final.next
            
            
        
        
        