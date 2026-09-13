# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:  
    def merge(self, head1, head2):
        if not head1:
            return head2

        if not head2:
            return head1

        if head1.val <= head2.val:
            head = head1
            head1 = head1.next
        else:
            head = head2
            head2 = head2.next

        current = head

        while head1 and head2:
            if head1.val <= head2.val:
                current.next = head1
                head1 = head1.next
            else:
                current.next = head2
                head2 = head2.next
        
            current = current.next

        if head1:
            current.next = head1
        if head2:
            current.next = head2

        return head

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        while len(lists) > 1:
            merged = []

            for i in range (0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i+1] if i+1 < len(lists) else None

                merged.append(self.merge(l1, l2))
            lists = merged
        
        return lists[0]
    