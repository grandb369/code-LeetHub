"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        k={}
        head=root=Node(node.val)
        seen=set([node.val])
        k[node.val]=root
        added=set([])
        stack=[node]
        while stack:
            temp=[]
            for i in stack:
                root=k[i.val]
                for j in i.neighbors:
                    if j.val not in seen:
                        k[j.val]=Node(j.val)
                    cur=k[j.val]
                    if cur.val not in added and i.val not in added:
                        root.neighbors.append(cur)
                        cur.neighbors.append(root)
                    if j.val not in seen:
                        seen.add(j.val)
                        temp.append(j)
                added.add(i.val)
            stack=temp
        return head