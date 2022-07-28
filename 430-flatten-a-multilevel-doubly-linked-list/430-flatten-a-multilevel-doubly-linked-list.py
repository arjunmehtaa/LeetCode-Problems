"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        current = head
        while current:
            if current.child:
                next = current.next
                current.next = current.child
                current.next.prev = current
                current.child = None
                last = current.next
                while last.next:
                    last = last.next
                last.next = next
                if next:
                    next.prev = last
            current = current.next
        return head

        