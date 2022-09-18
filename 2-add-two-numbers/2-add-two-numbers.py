# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        final = ListNode()
        head = final
        while l1 or l2:
            if l1 and l2:
                sum = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif not l1:
                sum = l2.val + carry
                l2 = l2.next
            else:
                sum = l1.val + carry
                l1 = l1.next
            carry = 0
            if sum > 9:
                sumStr = str(sum)
                carry = int(sumStr[0])
                sum = int(sumStr[1])
            final.next = ListNode(sum)
            final = final.next
        if carry > 0:
            final.next = ListNode(carry)
        return head.next