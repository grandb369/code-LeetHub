# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        out=ListNode()
        if not head:
            return head
        cur=head.next
        node=out
        while cur:
            val=0
            while cur and cur.val!=0:
                val+=cur.val
                cur=cur.next
            root=ListNode(val)
            node.next=root
            node=node.next
            cur=cur.next

        return out.next