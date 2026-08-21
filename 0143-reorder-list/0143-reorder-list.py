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
        if head is None or head.next is None:
            return 
        #find middle
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        #split list
        second=slow.next
        slow.next=None
        #reverse second half
        current=second
        prev=None
        while current:
            next_node=current.next
            current.next=prev
            prev=current
            current=next_node
        #merging two halves
        first=head
        second=prev
        while second:
            first_next=first.next
            second_next=second.next

            first.next=second
            second.next=first_next

            first=first_next
            second=second_next
