class Solution:
    def minWindow(self, s: str, t: str) -> str:
        import collections
        if len(t)>len(s):
            return ''
        import collections
        t=collections.Counter(t)
        ss=[(i,j)for i,j in enumerate(s) if j in t]
        ty=0
        l=r=0
        key=collections.defaultdict(int)
        out=''
        while r<len(ss):
            char=ss[r][1]
            key[char]+=1
            if key[char]==t[char]:
                ty+=1
            while ty==len(t) and l<=r:
                if not out or ss[r][0]-ss[l][0]+1<len(out):
                    out=s[ss[l][0]:ss[r][0]+1]
                char=ss[l][1]
                key[char]=max(key[char]-1,0)
                if key[char]<t[char]:
                    ty-=1
                l+=1
            r+=1
        return out