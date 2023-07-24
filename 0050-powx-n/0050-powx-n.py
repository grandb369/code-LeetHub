class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n<0:
            neg=True
            n*=-1
        elif n==0:
            return 1/1
        else:
            neg=False
        base=1
        incre=x
        out=1
        while n>0:
            n-=base
            out*=incre
            incre*=incre
            base+=base
            if base>n:
                base=1
                incre=x
        return out if not neg else 1/out