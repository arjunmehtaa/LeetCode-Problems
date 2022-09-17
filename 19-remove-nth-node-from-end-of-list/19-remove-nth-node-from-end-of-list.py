# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None
        current = head
        count = 1
        while count < n:
            count += 1
            current = current.next
        start = head
        prev = start
        while current.next:
            current = current.next
            prev = start
            start = start.next
            count += 1
        if count == n:
            return head.next
        prev.next = start.next
        start.next = None
        return head