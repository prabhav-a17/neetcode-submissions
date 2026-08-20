# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fp=head.next
        sp=head

        while fp and fp.next:
            if fp==sp:
                return True
            fp=fp.next.next
            sp=sp.next
        return False
        
