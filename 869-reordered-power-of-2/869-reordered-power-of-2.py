class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        temp=set([])
        base=1
        while base<=10**9:
            val=str(base)
            val=''.join(sorted(val))
            temp.add(val)
            base*=2
        n=str(N)
        n=''.join(sorted(n))
        return n in temp