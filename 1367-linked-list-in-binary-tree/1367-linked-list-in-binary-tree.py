# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubPath(self, head, root):
        """
        :type head: ListNode
        :type root: TreeNode
        :rtype: bool
        """
        self.out=[]
        def search(root,temp):
            temp+=str(root.val)
            if not root.left and not root.right:
                self.out.append(temp)
            if root.left:
                search(root.left,temp)
            if root.right:
                search(root.right,temp)
        search(root,'')
        val=''
        while head:
            val+=str(head.val)
            head=head.next
        for i in self.out:
            if val in i:
                return True
        return False
        