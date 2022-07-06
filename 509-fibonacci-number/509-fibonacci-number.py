class Solution:
    def fib(self, N: int) -> int:
        
        if N<2:
            return N
        pre=0
        cur=1
        for i in range(2,N+1):
            cur,pre=pre+cur,cur
        return cur