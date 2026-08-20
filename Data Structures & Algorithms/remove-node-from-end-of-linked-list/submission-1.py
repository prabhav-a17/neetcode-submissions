# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # OH but it is from the back of the list I see. 
        # So brute force would probably be reverse the list and then the take that out and then reverese it again but that would be like O(2N)
        # Is there a way I can do this differently probably.\
        dummy= ListNode(0, head)
        first = head
        second = dummy
        

        for i in range(n):
            first= first.next
        
        while first:
            first= first.next
            second = second.next

        second.next=second.next.next
        return dummy.next

        
