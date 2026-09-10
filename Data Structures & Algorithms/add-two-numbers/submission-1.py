# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, head1: Optional[ListNode], head2: Optional[ListNode]) -> Optional[ListNode]:
        if not head1:
            return head2
        if not head2:
            return head1
        
        total = 0
        carry = 0
        prev = None
        head = head1

        while head1 and head2:
            total = head1.val + head2.val + carry
            head1.val = total % 10
            carry = total // 10
            prev = head1
            head1 = head1.next
            head2 = head2.next

        if head2:
            prev.next = head2
            while head2:
                total = head2.val + carry
                head2.val = total % 10
                carry = total // 10
                prev = head2
                head2 = head2.next

            
        if head1:
            while head1:
                total = head1.val + carry
                head1.val = total % 10
                carry = total // 10
                prev = head1
                head1 = head1.next
        if carry > 0:
            prev.next = ListNode(carry)
    

        return head


        