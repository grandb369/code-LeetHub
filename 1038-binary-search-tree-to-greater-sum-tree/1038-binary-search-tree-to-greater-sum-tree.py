# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        temp=0
        out=root
        stack=[root]
        while stack:
            root=stack.pop()
            while root:
                stack.append(root.left)
                stack.append(root)
                root=root.right
            if stack:
                root=stack.pop()
                root.val+=temp
                temp=root.val
        return out