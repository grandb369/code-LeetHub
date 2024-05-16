# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if root:
                if root.val ==0 or root.val==1:
                    return root.val
                left=dfs(root.left)
                right=dfs(root.right)
                if root.val==2:
                    return left or right
                return left and right
        return dfs(root)