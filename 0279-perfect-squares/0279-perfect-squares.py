class Solution:
    def numSquares(self, n: int) -> int:
        if n <2:
            return n
        sq=[]
        i=1
        while i**2<=n:
            sq.append(i**2)
            i+=1
        stack=[n]
        out=1
        while stack:
            temp=set()
            for i in stack:
                for j in sq:
                    if j==i:
                        return out
                    elif j>i:
                        break
                    temp.add(i-j)
            stack=temp
            out+=1
        return out