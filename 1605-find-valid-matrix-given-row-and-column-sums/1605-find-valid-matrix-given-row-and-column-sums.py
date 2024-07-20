class Solution:
    def restoreMatrix(self, row: List[int], col: List[int]) -> List[List[int]]:
        n=len(row)
        m=len(col)
        out=[[0 for i in range(m)]for i in range(n)]
        i=0
        j=0
        while i<n and j<m:
            c=col[j]
            r=row[i]
            val=min(r,c)
            out[i][j]=val
            row[i]-=val
            col[j]-=val
            if val==r==c:
                i+=1
                j+=1
            elif val==r:
                i+=1
            else:
                j+=1
        return out
                