class tree:
    def __init__(self):
        self.head={}
        self.data=set([])
    
    def update(self,i, s):
        if i<len(s):
            cur=s[i]
            if cur not in self.head:
                self.head[cur]=tree()
            self.head[cur].data.add(s)
            self.head[cur].update(i+1,s)
    def get(self, i, s, out):
        if i<len(s):
            cur=s[i]
            if i!=0:
                out.append(sorted(self.data)[:3])
            if cur not in self.head:
                for i in range(len(s)-len(out)):
                    out.append([])
            else:
                self.head[cur].get(i+1,s,out)
        elif i==len(s):
            out.append(sorted(self.data)[:3])
class Solution:
    def suggestedProducts(self, p: List[str], q: str) -> List[List[str]]:
        t=tree()
        for s in p:
            t.update(0,s)
        out=[]
        t.get(0,q,out)
        return out