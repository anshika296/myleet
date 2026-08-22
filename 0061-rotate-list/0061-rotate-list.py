# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        count=0
        current=head
        while current:
            count+=1
            if current.next is None:
                tail=current
            current=current.next
        k=k%count #if its greater than length
        count=count-k
        if k==0:
            return head
        
        temp=head
        for i in range(count-1):
            temp=temp.next
        second=temp.next
        temp.next=None
        tail.next=head
        return second

        