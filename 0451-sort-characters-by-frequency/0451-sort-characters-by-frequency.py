class Solution:
    def frequencySort(self, s: str) -> str:
        k=collections.defaultdict(int)
        for i in s:
            k[i]+=1
        out=''.join([i*k[i] for i in sorted(k.keys(),key=lambda x:k[x], reverse=True)])
        return out