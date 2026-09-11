# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        curr1=l1
        prev=None
        while curr1:
            next_node=curr1.next
            curr1.next=prev
            prev=curr1
            curr1=next_node
        curr2=l2
        prev2=None
        while curr2:
            next_node2=curr2.next
            curr2.next=prev2
            prev2=curr2
            curr2=next_node2
        str1=""
        while prev:
            str1+=str(prev.val)
            prev=prev.next
        str2=""
        while prev2:
            str2+=str(prev2.val)
            prev2=prev2.next
        num1=int(str1)
        num2=int(str2)
        ans=num1+num2
        list1=[]
        if ans==0:
            list1.append(0)
        while ans>0:
            dig=ans%10
            list1.append(dig)
            ans=ans//10
        head=ListNode(list1[0])
        current=head
        for i in list1[1:]:
            current.next=ListNode(i)
            current=current.next
        return head
        


        