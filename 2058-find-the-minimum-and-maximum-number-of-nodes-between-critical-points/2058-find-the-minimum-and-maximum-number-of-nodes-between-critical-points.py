# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        temp=[]
        pre=None
        c=0
        while head:
            nex=head.next
            if pre and nex:
                if pre.val>head.val and nex.val>head.val:
                    temp.append(c)
                elif pre.val<head.val and head.val>nex.val:
                    temp.append(c)
            pre=head
            c+=1
            head=head.next
        if len(temp)<2:
            return [-1,-1]
        out=[temp[-1]-temp[0],temp[-1]-temp[0]]
        for i in range(1,len(temp)):
            out[0]=min(out[0],temp[i]-temp[i-1])
        return out