# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        sec = slow.next
        slow.next = None
        
        prev = None
        while sec:
            next = sec.next
            sec.next = prev
            prev = sec
            sec = next
        
        l1 = head
        l2 = prev
        final = ListNode()
        ans = final
        while l1 and l2:
            final.next = l1
            l1 = l1.next
            final = final.next
            final.next= l2
            l2 = l2.next
            final = final.next
        final.next = l1 or l2
        return ans.next
            
        