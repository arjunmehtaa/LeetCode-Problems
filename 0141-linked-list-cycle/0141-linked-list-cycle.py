# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Optimal Solution
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        a = head
        b = head
        while b.next and b.next.next:
            a = a.next
            b = b.next.next
            if a == b:
                return True
        return False

# Brute Force Solution
# Time Complexity: O(N)
# Space Complexity: O(N)

# class Solution:
#     def hasCycle(self, head: Optional[ListNode]) -> bool:
#         current = head
#         data = set()
#         if current == None:
#             return False
#         while current not in data:
#             if not current.next:
#                 return False
#             data.add(current)
#             current = current.next
#         return True