# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        start = head
        link = head
        while count < left:
            link = start
            start = start.next
            count += 1
        prev = None
        current = start
        while count <= right:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
        start.next = current
        if left == 1:
            return prev
        else:
            link.next = prev
            return head

        