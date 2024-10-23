# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack=[root]
        root.val=0
        while stack:
            nex=[]
            n=len(stack)
            temp=[0 for i in range(n)]
            for i in range(n):
                cur=stack[i]
                if cur.left:
                    nex.append(cur.left)
                    temp[i]+=cur.left.val
                if cur.right:
                    nex.append(cur.right)
                    temp[i]+=cur.right.val
            su=sum(temp)
            for i in range(n):
                cur=stack[i]
                if cur.left:
                    cur.left.val=su-temp[i]
                if cur.right:
                    cur.right.val=su-temp[i]
            stack=nex
        return root