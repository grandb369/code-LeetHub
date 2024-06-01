class Solution:
    def compareVersion(self, s1: str, s2: str) -> int:
        s1=s1.split('.')
        s2=s2.split('.')
        def remove(s):
            out=[]
            for i in s:
                v=list(i)[::-1]
                while len(v)>1 and v[-1]=='0':
                    v.pop()
                out.append(''.join(v[::-1]))
            return out
        s1=remove(s1)
        s2=remove(s2)
        while len(s1)>1 and s1[-1]=='0':
            s1.pop()
        while len(s2)>1 and s2[-1]=='0':
            s2.pop()
        for i in range(min(len(s1),len(s2))):
            v1=int(s1[i])
            v2=int(s2[i])
            if v1>v2:
                return 1
            if v2>v1:
                return -1
        if len(s1)>len(s2):
            return 1
        if len(s2)>len(s1):
            return -1
        return 0