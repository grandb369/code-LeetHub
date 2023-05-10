class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        out=[[0 for i in range(n)]for i in range(n)]
        cur=1
        for i in range(n//2+n%2):
            for j in range(i,n-i):
                out[i][j]=cur
                cur+=1
            if i==n//2+n%2-1 and n%2:
                break
            for j in range(i+1,n-i):
                out[j][n-1-i]=cur
                cur+=1
            for j in range(n-i-2,i-1,-1):
                out[n-i-1][j]=cur
                cur+=1
            for j in range(n-i-2,i,-1):
                out[j][i]=cur
                cur+=1
        return out