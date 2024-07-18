# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if not root:
            return 0
        self.out=0
        def dfs(root):
            if not root.left and not root.right:
                return [1]
            elif root.left and root.right:
                left=dfs(root.left)
                right=dfs(root.right)
                for i in left:
                    for j in right:
                        if i+j<=distance:
                            self.out+=1
                val=left+right
                for i in range(len(val)):
                    val[i]+=1
                return val
            val=[]
            if root.left:
                val=dfs(root.left)
            if root.right:
                val=dfs(root.right)
            val=[i+1for i in val]
            return val
        dfs(root)
        return self.out