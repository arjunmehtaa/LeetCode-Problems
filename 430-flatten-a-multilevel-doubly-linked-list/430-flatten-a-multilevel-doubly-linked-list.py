"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head
        while current:
            if current.child:
                old_next = current.next
                current.next = current.child
                current.child = None
                current.next.prev = current
                active = current
                while active.next:
                    active = active.next
                active.next = old_next
                if old_next:
                    old_next.prev = active
            current = current.next
        return head
        