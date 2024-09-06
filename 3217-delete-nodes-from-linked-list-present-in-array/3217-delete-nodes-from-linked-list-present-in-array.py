# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        out=ListNode()
        out.next=head
        nums=set(nums)
        head=out
        while head and head.next:
            if head.next.val in nums:
                head.next=head.next.next
            else:
                head=head.next
        return out.next