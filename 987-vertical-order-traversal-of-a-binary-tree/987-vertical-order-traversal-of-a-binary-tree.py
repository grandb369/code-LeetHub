# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        k=collections.defaultdict(list)
        out=[]
        if not root:
            return []
        stack=[(root,0)]
        while stack:
            temp=collections.defaultdict(list)
            nex=[]
            for i,l in stack:
                temp[l].append(i.val)
                if i.left:
                    nex.append((i.left,l-1))
                if i.right:
                    nex.append((i.right,l+1))
            for i in temp:
                k[i]+=sorted(temp[i])
            stack=nex
        for i in sorted(k.keys()):
            out.append(k[i])
        return out