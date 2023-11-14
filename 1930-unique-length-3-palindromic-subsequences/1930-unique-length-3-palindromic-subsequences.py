class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        out=set([])
        k=collections.defaultdict(list)
        for i,j in enumerate(s):
            k[j].append(i)
        for i in k:
            if len(k[i])<2:
                continue
            l=k[i][0]
            r=k[i][-1]
            for j in set([s[x]for x in range(l+1,r)]):
                out.add(i+j+i)
        return len(out)