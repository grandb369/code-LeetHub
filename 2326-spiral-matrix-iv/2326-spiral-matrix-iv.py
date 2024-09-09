# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, n: int, m: int, head: Optional[ListNode]) -> List[List[int]]:
        out=[[-1 for i in range(m)]for i in range(n)]
        seen=set([])
        r,c=0,0
        di=(0,1)
        rt=0
        cl=0
        while (r,c)not in seen and head and rt<=r and r<n and cl<=c and c<m:
            #print(r,c)
            out[r][c]=head.val
            head=head.next
            seen.add((r,c))
            if di==(0,1):
                if c+1<m:
                    c+=1
                else:
                    rt+=1
                    di=(1,0)
                    r+=1
            elif di==(1,0):
                if r+1<n:
                    r+=1
                else:
                    m-=1
                    di=(0,-1)
                    c-=1
            elif di==(0,-1):
                if c-1>=cl:
                    c-=1
                else:
                    n-=1
                    di=(-1,0)
                    r-=1
            else:
                if r-1>=rt:
                    r-=1
                else:
                    cl+=1
                    di=(0,1)
                    c+=1
        return out