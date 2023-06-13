class Solution:
    def equalPairs(self, mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        for r in range(n):
            for c in range(m):
                mat[r][c]=str(mat[r][c])
        row=collections.defaultdict(int)
        col=collections.defaultdict(int)
        nums=[[''for j in range(n)] for i in range(m)]
        for r in range(n):
            for c in range(m):
                nums[c][r]=mat[r][c]
            rr=','.join(mat[r])
            row[rr]+=1
        for c in range(m):
            cc=','.join(nums[c])
            col[cc]+=1
        out=0
        for i in row:
            if i in col:
                out+=row[i]*col[i]
        return out