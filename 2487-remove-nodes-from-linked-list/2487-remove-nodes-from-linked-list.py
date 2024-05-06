# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack=[]
        while head:
            while stack and stack[-1].val<head.val:
                stack.pop()
            root=head
            head=head.next
            root.next=None
            stack.append(root)
        out=ListNode()
        root=out
        for r in stack:
            root.next=r
            root=r
        return out.next