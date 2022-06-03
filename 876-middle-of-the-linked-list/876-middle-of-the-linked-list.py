# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre=ListNode()
        pre.next=head
        p1=p2=pre
        while p1:
            p1=p1.next
            if p1:
                p1=p1.next
            p2=p2.next
        return p2