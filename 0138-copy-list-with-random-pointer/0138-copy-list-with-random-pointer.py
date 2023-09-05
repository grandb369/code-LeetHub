"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        root=head
        if not head:
            return None
        while root:
            node=Node(root.val)
            node.next=root.next
            root.next=node
            root=node.next
        root=head
        while root:
            node=root.next
            if root.random:
                ran=root.random
                node.random=ran.next
            root=node.next
        root=head
        out=head.next
        while root:
            nex=root.next
            root.next=nex.next
            if nex.next:
                nex.next=nex.next.next
            root=root.next
        return out