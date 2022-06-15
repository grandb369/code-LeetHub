class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        k=collections.defaultdict(set)
        out={i:1 for i in words}
        for i in words:
            k[len(i)].add(i)
        for i in sorted(k.keys(),reverse=True):
            if i-1 in k:
                for w in k[i]:
                    for j in range(len(w)):
                        s=w[:j]+w[j+1:]
                        if s in k[i-1]:
                            out[s]=max(out[s],out[w]+1)
        return max(out.values())
                    