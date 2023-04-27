class Solution:
    def bulbSwitch(self, n: int) -> int:
        out=0
        v=1
        val=1
        while val<=n:
            out+=1
            v+=1
            val=v**2
        return out