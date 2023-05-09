class Solution:
    def spiralOrder(self, mat: List[List[int]]) -> List[int]:
        out=[]
        n=len(mat)
        m=len(mat[0])
        if n==1:
            return mat[0]
        if m==1:
            return [i[0] for i in mat]
        for i in range(min(n//2+n%2,m//2+m%2)):
            l=i
            r=m-i-1
            up=i+1
            down=n-i-2
            #print(l,r,up,down)
            for j in range(l,r+1):
                out.append(mat[i][j])
            for j in range(up,down+1):
                out.append(mat[j][r])
            if i!=n-i-1:
                for j in range(r,l-1,-1):
                    out.append(mat[down+1][j])
            if l!=r:
                for j in range(down,up-1,-1):
                    out.append(mat[j][i])
        return out 