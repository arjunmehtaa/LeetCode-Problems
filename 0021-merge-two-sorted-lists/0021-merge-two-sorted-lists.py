# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Time Complexity	: O(N + M)
# Space Complexity	: O(N + M)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        final = ListNode()
        head = final
        while list1 and list2:
            if list1.val < list2.val:
                final.next = list1
                list1 = list1.next
            else:
                final.next = list2
                list2 = list2.next
            final = final.next
        final.next = list1 or list2
        return head.next