class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        temp=set([])
        n=len(s)
        if len(s)==1:
            return False
        elif len(set(s))==1:
            return True
        i=2
        while i<=n//i:
            if n%i==0:
                temp.add((i,n//i))
            i+=1
        #print(temp)
        for i,j in temp:
            v=s[:i]
            ans=True
            for k in range(i,n,i):
                #print(s[k:k+i],v)
                if s[k:k+i]!=v:
                    ans=False
                    break
            if ans:
                return True
            v=s[:j]
            ans=True
            for k in range(j,n,j):
                #print(s[k:k+j],v)
                if s[k:k+j]!=v:
                    ans=False
                    break
            if ans:
                return True
        return False