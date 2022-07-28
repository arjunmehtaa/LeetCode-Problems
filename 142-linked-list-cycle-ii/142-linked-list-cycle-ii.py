# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        a = head
        b = head
        current = head
        if head == None:
            return None
        while True:
            a = a.next
            b = b.next
            if not b or not b.next:
                return None
            else:
                b = b.next
            if a == b:
                break
        while current != b:
            current = current.next
            b = b.next
        return current
    