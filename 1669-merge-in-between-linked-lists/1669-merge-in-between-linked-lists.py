# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, l1: ListNode, a: int, b: int, l2: ListNode) -> ListNode:
        head=p1=ListNode(0)
        head.next=l1
        while a>0 and p1:
            p1=p1.next
            a-=1
            b-=1
        if p1:
            p2=p1.next
        while b>0 and p2:
            p2=p2.next
            b-=1
        if p2:
            p3=p2.next
            p2.next=None
        p4=l2
        while p4.next:
            p4=p4.next
        p1.next=l2
        p4.next=p3
        return head.next