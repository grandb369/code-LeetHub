class Solution:
    def validWordAbbreviation(self, s1: str, s2: str) -> bool:
        s1=list(s1)
        s2=list(s2)
        while s2:
            if s2[-1].isdigit():
                cur=''
                while s2 and s2[-1].isdigit():
                    cur=s2.pop()+cur
            else:
                cur=s2.pop()
            
            if cur.isdigit():
                if cur[0]=='0':
                    return False
                c=int(cur)
                while s1 and c:
                    c-=1
                    s1.pop()
                if c:
                    return False
            else:
                if not s1 or s1.pop()!=cur:
                    return False
        return len(s1)==0