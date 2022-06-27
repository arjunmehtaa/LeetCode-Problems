# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseLinkedList(head: ListNode, left: int, right: int) -> ListNode:
    current = head
    count = left
    prev = None
    prev_tail = prev
    while current and count <= right:
        next = current.next
        current.next = prev
        prev = current
        current = next
        count += 1
    head.next = current
    return prev

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        current = head
        prev = current
        while count < left:
            prev = current
            current = current.next
            count += 1
        if left > 1:
            prev.next = reverseLinkedList(current, left, right)
            return head
        else:
            return reverseLinkedList(current, left, right)
        

        