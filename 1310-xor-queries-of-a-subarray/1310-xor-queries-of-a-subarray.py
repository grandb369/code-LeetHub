class Solution:
    def xorQueries(self, arr: List[int], q: List[List[int]]) -> List[int]:
        p=[i for i in arr]
        n=len(arr)
        for i in range(1,n):
            p[i]^=p[i-1]
        out=[]
        for l,r in q:
            if l>0:
                out.append(p[r]^p[l-1])
            else:
                out.append(p[r])
        return out