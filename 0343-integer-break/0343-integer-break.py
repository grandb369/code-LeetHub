class Solution:
    def integerBreak(self, n: int) -> int:
        k={}
        k[1]=1
        k[2]=1
        k[3]=2
        k[4]=4
        k[5]=6
        k[6]=9
        for i in range(7,n+1):
            val=0
            j=2
            while i-j>1:
                if k[i-j]*j<val:
                    break
                else:
                    val=max(val,k[i-j]*j)
                j+=1
            k[i]=val
        return k[n]