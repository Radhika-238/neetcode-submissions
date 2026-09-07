# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        first_half = head
        second_half = slow.next
        slow.next = None

        #reverse second half

        prev = None
        current = second_half

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        #merge

        head1 = first_half
        head2 = prev

        while head1 and head2:
            temp1 = head1.next
            temp2 = head2.next
            head1.next = head2
            head2.next = temp1
            head1 = temp1
            head2 = temp2
            

