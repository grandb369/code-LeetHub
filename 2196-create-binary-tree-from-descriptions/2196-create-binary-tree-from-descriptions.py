# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, nums: List[List[int]]) -> Optional[TreeNode]:
        k={}
        node=set([])
        count=collections.defaultdict(int)
        for pre,child,left in nums:
            node.add(pre)
            node.add(child)
            if pre not in k:
                pre=TreeNode(pre)
                k[pre.val]=pre
            else:
                pre=k[pre]
            if child not in k:
                child=TreeNode(child)
                k[child.val]=child
            else:
                child=k[child]
            if left==1:
                pre.left=child
            else:
                pre.right=child
            count[child.val]+=1
        for i in node:
            if i not in count:
                return k[i]