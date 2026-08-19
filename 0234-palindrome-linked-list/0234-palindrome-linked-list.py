# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        #find middle
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        #reverse the second half
        prev=None
        current=slow
        while current:
            next=current.next
            current.next=prev
            prev=current
            current=next
        #compare
        left=head
        right=prev
        while right:
            if left.val!=right.val:
                return False
            left=left.next
            right=right.next
        return True


        
        