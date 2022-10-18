class Solution:
    def countAndSay(self, n: int) -> str:
        out='1'
        if n==1:
            return out
        out='11'
        if n==2:
            return out
        for i in range(3,n+1):
            p1=0
            p2=1
            temp=''
            while p2<len(out):
                if out[p2]!=out[p1]:
                    temp+=str(p2-p1)+out[p1]
                    p1=p2
                    p2+=1
                    if p2==len(out):
                        temp+='1'+out[p1]
                else:
                    if p2==len(out)-1:
                        temp+=str(p2-p1+1)+out[p1]
                    p2+=1
            out=temp
        return out