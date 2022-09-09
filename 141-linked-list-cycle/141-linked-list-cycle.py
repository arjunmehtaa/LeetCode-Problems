# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        a = head
        b = head.next
        while b and b.next:
            if a == b:
                return True
            a = a.next
            b = b.next.next
        return False