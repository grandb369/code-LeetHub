# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        p1=p2=head
        while n!=0 and p1.next:
            n-=1
            p1=p1.next
        if n!=0:
            return head.next
            
        while p1 and p1.next:
            p1=p1.next
            p2=p2.next
        if p2 and p2.next:
            p2.next=p2.next.next
        return head