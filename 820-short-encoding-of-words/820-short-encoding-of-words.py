class Trie:
    def __init__(self):
        self.data={}

    def update(self, i, s):
        if i>=0:
            cur=s[i]
            if s[i] not in self.data:
                self.data[cur]=Trie()
            self.data[cur].update(i-1, s)
    
    def search(self, pre):
        if not self.data:
            return pre+1 if pre else 0
        out=0
        for nex in self.data:
            out+=self.data[nex].search(pre+1)
        return out
            
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        tree=Trie()
        for s in words:
            tree.update(len(s)-1, s)
        out=tree.search(0)
        return out