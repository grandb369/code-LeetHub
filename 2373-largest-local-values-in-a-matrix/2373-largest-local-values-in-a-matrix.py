class Solution:
    def largestLocal(self, mat: List[List[int]]) -> List[List[int]]:
        n=len(mat)
        out=[]
        for i in range(n-2):
            temp=[]
            for j in range(n-2):
                val=0
                for x in range(i,i+3):
                    for y in range(j,j+3):
                        val=max(val,mat[x][y])
                temp.append(val)
            out.append(temp)
        return out