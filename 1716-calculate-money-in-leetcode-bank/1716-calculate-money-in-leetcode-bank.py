class Solution:
    def totalMoney(self, n: int) -> int:
        out=0
        base=1
        while n>0:
            val=min(7,n)
            for i in range(val):
                out+=base+i
            base+=1
            n-=val
        return out