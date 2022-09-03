class Solution:
    def numsSameConsecDiff(self, N: int, K: int) -> List[int]:
        def back(out,temp,n,k):
            if n==0:
                out.append(int(temp))
            else:
                v=int(temp[-1])
                if v-k>=0:
                    back(out,temp+str(v-k),n-1,k)
                if v+k<10 and k!=0:
                    back(out,temp+str(v+k),n-1,k)
        out=[]
        for i in range(1,10):
            back(out,str(i),N-1,K)
        return out