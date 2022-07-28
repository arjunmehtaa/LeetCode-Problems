# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return None
        a = head
        b = head
        while b.next:
            a = a.next
            b = b.next
            if not b.next:
                return None
            else:
                b = b.next
            if a == b:
                while head != a:
                    head = head.next
                    a = a.next
                return a
        return None