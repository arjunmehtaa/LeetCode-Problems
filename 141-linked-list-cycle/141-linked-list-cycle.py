# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        current = head
        data = set()
        if current == None:
            return False
        while current not in data:
            if not current.next:
                return False
            data.add(current)
            current = current.next
        return True