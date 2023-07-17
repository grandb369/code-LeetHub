# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        v1=v2=0
        while l1:
            v1=v1*10+l1.val
            l1=l1.next
        while l2:
            v2=v2*10+l2.val
            l2=l2.next
        val=v1+v2
        if val==0:
            return ListNode(0)
        pre=None
        while val>0:
            root=ListNode(val%10)
            root.next=pre
            pre=root
            val//=10
        return pre