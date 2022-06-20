class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        out=0
        k={}
        words.sort(key=lambda x:len(x),reverse=True)
        for w in words:
            new=False
            cur=k
            for j in range(len(w)-1,-1,-1):
                if w[j] not in cur:
                    new=True
                    cur[w[j]]={}
                cur=cur[w[j]]
            if new==True:
                out+=len(w)+1
        return out