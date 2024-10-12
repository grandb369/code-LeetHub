class Tree:
    def __init__(self):
        self.data={}
        self.c=0
class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        tree=Tree()
        for w in words:
            t=tree
            for i in w:
                if i not in t.data:
                    t.data[i]=Tree()
                t=t.data[i]
                t.c+=1
        out=[]
        for w in words:
            t=tree
            val=0
            for i in w:
                t=t.data[i]
                val+=t.c
            out.append(val)
        return out