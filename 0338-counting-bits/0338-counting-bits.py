class Solution:
    def countBits(self, n: int) -> List[int]:
        out=[0]
        base=1
        for i in range(1,n+1):
            if i==base:
                out.append(1)
                base*=2
            else:
                out.append(1+out[i-base])
        return out