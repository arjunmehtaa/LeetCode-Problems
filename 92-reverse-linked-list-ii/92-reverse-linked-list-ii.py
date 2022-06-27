# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        count = 1
        current = head
        prev = current
        
        while count < left:
            prev = current
            current = current.next
            count += 1     
            
        reversed_head = None
        tail = current
        
        while count <= right:
            next = current.next
            current.next = reversed_head
            reversed_head = current
            current = next
            count += 1
            
        prev.next = reversed_head
        tail.next = current
        
        if left > 1:
            return head
        else:
            return reversed_head
        

        