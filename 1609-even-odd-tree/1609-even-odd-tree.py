# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        level=0
        stack=[root]
        while stack:
            temp=[]
            ans=[]
            for i in stack:
                if ans:
                    if level%2==0:
                        if i.val%2==0 or i.val<=ans[-1]:
                            return False
                    if level%2==1:
                        if i.val%2==1 or i.val>=ans[-1]:
                            return False
                else:
                    if level%2==0 and i.val%2==0:
                        return False
                    if level%2==1 and i.val%2==1:
                        return False
                ans.append(i.val)
                if i.left:
                    temp.append(i.left)
                if i.right:
                    temp.append(i.right)
            stack=temp
            level+=1
        return True