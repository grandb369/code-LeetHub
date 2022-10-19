class Solution:
    def topKFrequent(self, words: List[str], c: int) -> List[str]:
        k=collections.defaultdict(int)
        for i in words:
            k[i]+=1
        w=collections.defaultdict(set)
        for i in k:
            w[k[i]].add(i)
        out=[]
        for i in sorted(w.keys(),reverse=True):
            if c>=len(w[i]):
                out+=sorted(w[i])
            else:
                out+=sorted(w[i])[:c]
            c-=len(w[i])
            if c<1:
                break
        return out