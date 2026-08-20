# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 2->4->6->8
        #Ok so I am alternating between the end and the beginning?
        # So I go add the head then I add then end but yeah here we arent given the tail or anything

        sp=head
        fp=head.next

        while fp and fp.next:
            fp=fp.next.next
            sp=sp.next
        
        curr=sp.next
        prev=sp.next=None

        while curr:
            temp= curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        second = prev
        first = head

        while second:
            temp1= first.next
            temp2= second.next
            first.next=second
            second.next=temp1
            second=temp2
            first=temp1




            
        
