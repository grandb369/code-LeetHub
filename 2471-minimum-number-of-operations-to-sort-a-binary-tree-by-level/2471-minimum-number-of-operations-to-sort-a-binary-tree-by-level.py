# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        out=0
        stack=[root]
        while stack:
            temp=[]
            nex=[]
            k={}
            c=0
            for root in stack:
                if root.left:
                    temp.append(root.left)
                    nex.append(root.left)
                    k[root.left]=c
                    c+=1
                if root.right:
                    temp.append(root.right)
                    nex.append(root.right)
                    k[root.right]=c
                    c+=1
            so=sorted(temp,key=lambda x:x.val)
            c=0
            while so:
                cur=so.pop()
                if temp[-1]==cur:
                    temp.pop()
                else:
                    index=k[cur]
                    k[temp[-1]]=index
                    temp[index]=temp[-1]
                    temp.pop()
                    c+=1
            out+=c
            stack=nex
        return out