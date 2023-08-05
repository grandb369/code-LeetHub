# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        nums=[i for i in range(1,n+1)]
        def build(nums):
            if not nums:
                return []
            out=[]
            for i in range(len(nums)):
                left=build(nums[:i])
                right=build(nums[i+1:])
                if not left and not right:
                    out.append(TreeNode(nums[i]))
                if left and right:
                    for l in left:
                        for r in right:
                            root=TreeNode(nums[i])
                            root.left=l
                            root.right=r
                            out.append(root)
                elif left:
                    for l in left:
                        root=TreeNode(nums[i])
                        root.left=l
                        out.append(root)
                else:
                    for r in right:
                        root=TreeNode(nums[i])
                        root.right=r
                        out.append(root)
            return out
        return build(nums)