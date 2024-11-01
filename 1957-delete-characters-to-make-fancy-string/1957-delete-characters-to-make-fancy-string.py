class Solution:
    def makeFancyString(self, s: str) -> str:
        c=1
        out=pre=s[0]
        s=s[1:]
        for i in s:
            if i==pre:
                if c<2:
                    c+=1
                    out+=i
                else:
                    c+=1
            else:
                out+=i
                pre=i
                c=1
        return out