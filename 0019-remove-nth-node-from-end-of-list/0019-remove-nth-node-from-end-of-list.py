# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter = 1
        current = head
        while counter < n:
            counter += 1
            current = current.next
        prev = head
        start = head
        while current.next:
            prev = start
            start = start.next
            current = current.next
            counter += 1
        if counter == n:
            return head.next
        prev.next = start.next
        start.next = None
        return head
            