# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        cur=1
        head=TreeNode()
        head.left=root
        stack=[head]
        out=head
        while stack:
            nex=[]
            for node in stack:
                if cur==depth:
                    left=node.left
                    node2=TreeNode(val)
                    node.left=node2
                    node2.left=left

                    right=node.right
                    node2=TreeNode(val)
                    node.right=node2
                    node2.right=right
                else:
                    if node.left:
                        nex.append(node.left)
                    if node.right:
                        nex.append(node.right)
            stack=nex
            cur+=1
        return out.left