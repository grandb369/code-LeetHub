# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre=ListNode(head)
        pre.next=head
        c=0
        p1=head
        while p1:
            c+=1
            p1=p1.next
        c//=2
        if c==0:
            return None
        if c==1:
            head.next=head.next.next
            return head
        p1=pre
        while c:
            p1=p1.next
            c-=1
        p1.next=p1.next.next
        return head