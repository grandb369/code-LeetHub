# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        out=ListNode()
        out.next=head
        pre=out
        cur=head
        while cur and cur.next:
            nex=cur.next
            temp=nex.next
            pre.next=nex
            nex.next=cur
            cur.next=temp
            pre=cur
            cur=cur.next
        return out.next