# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        def depth(root):
            if not root:
                return 0
            out=1
            while root.left:
                root=root.left
                out+=1
            return out
        out=0
        while root:
            left=depth(root.left)
            right=depth(root.right)
            if left==right:
                out+=2**(left)
                root=root.right
            else:
                out+=2**(right)
                root=root.left
        return out