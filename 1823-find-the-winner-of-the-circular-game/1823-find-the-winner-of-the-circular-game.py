class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        out=[i for i in range(1,n+1)]
        cur=0
        while len(out)>1:
            cur+=(k-1)
            cur%=len(out)
            out.pop(cur)
        return out[0]