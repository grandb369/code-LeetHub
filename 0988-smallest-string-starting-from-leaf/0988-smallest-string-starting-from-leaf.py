# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        self.out=None
        def dfs(pre, root):
            cur=chr(97+root.val)+pre
            if not root.left and not root.right:
                if not self.out or self.out>cur:
                    self.out=cur
            if root.left:
                dfs(cur, root.left)
            if root.right:
                dfs(cur, root.right)
        dfs("",root)
        return self.out