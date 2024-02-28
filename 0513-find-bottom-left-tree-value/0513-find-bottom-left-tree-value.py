# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return 
        stack=[root]
        last=[]
        while stack:
            temp=[]
            for i in stack:
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            last=stack
            stack=temp
        return last[0].val