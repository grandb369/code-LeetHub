# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        self.out=[]
        delete=set(to_delete)
        def search(root):
            if root:
                if root.val in delete:
                    delete.remove(root.val)
                    left=search(root.left)
                    right=search(root.right)
                    if left:
                        self.out.append(left)
                    if right:
                        self.out.append(right)
                    return None
                root.left=search(root.left)
                root.right=search(root.right)
                return root
        root=search(root)
        if root:
            self.out=[root]+self.out
        return self.out