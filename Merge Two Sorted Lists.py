# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None and list2 == None:
            return None
        head = final = ListNode()
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                final.next = list1
                list1 = list1.next                   
            else:
                final.next = list2
                list2 = list2.next
            final = final.next
        final.next = list1 or list2
        return head.next
        
