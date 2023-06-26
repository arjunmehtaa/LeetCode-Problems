# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        current = head
        i = 1
        while i < n:
            current = current.next
            i += 1
        start = head
        prev = start
        while current.next:
            prev = start
            start = start.next
            current = current.next
            i += 1
        prev.next = start.next
        if i == n:
            return head.next
        
        return head
            