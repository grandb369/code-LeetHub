# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or head.next==None:
            return head
        p1=p2=head.next
        head.next=None
        while p1!=None:
            p1=p1.next
            p2.next=head
            head=p2
            p2=p1
        return head
            