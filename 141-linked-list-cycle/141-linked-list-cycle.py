# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        if not head.next:
            return False
        a = head
        b = head.next
        while b:
            if b == a:
                return True
            a = a.next
            if not b.next:
                return False
            b = b.next.next 
        return False
