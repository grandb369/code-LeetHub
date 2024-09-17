class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=s1.split()
        s2=s2.split()
        s=set(s1+s2)
        s1=collections.Counter(s1)
        s2=collections.Counter(s2)
        out=[]
        for i in s:
            if i in s1 and i in s2:
                continue
            elif i in s1 and s1[i]==1:
                out.append(i)
            elif i in s2 and s2[i]==1:
                out.append(i)
        return out