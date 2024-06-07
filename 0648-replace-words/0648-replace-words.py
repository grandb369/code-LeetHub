class Node:
    def __init__(self,x=None):
        self.key=x
        self.child={}
        self.sen=''
        self.end=False
class Trie:
    def __init__(self):
        self.root=Node()
    def insert(self,x):
        root=self.root
        sen=''
        for i in x:
            if i not in root.child:
                root.child[i]=Node(i)
            sen+=i
            root=root.child[i]
        root.sen=sen
        root.end=True
    def replace(self,x):
        root=self.root
        for i in x:
            if root.end:
                return root.sen
            elif i not in root.child:
                return x
            root=root.child[i]
        return root.sen if root.end else x
class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        node=Trie()
        for i in dict:
            node.insert(i)
        sen=sentence.split()
        for i in range(len(sen)):
            sen[i]=node.replace(sen[i])
        return ' '.join(sen)