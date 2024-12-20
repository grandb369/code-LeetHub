# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        l=0
        out=root
        stack=[root]
        pre=[]
        while stack:
            nex=[]
            temp=[]
            for root in stack:
                if root.left:
                    nex.append(root.left)
                if root.right:
                    nex.append(root.right)
                if l%2:
                    temp.append(root.left)
                    temp.append(root.right)
            if l%2:
                i=0
                for root in pre:
                    root.left=stack.pop()
                    root.left.left=temp[i]
                    i+=1
                    root.left.right=temp[i]
                    i+=1
                    root.right=stack.pop()
                    root.right.left=temp[i]
                    i+=1
                    root.right.right=temp[i]
                    i+=1
            pre=stack
            stack=nex
            l+=1
        return out