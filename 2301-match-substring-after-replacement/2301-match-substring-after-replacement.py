class Solution:
    def matchReplacement(self, s: str, t: str, m: List[List[str]]) -> bool:
        if t in s:
            return True
        if len(t)>len(s):
            
            return False
        ss=set(list(s))
        k=collections.defaultdict(set)
        for i,j in m:
            if j in ss:
                k[j].add(i)
            else:
                for x in k.keys():
                    if j in k[x]:
                        k[x].add(i)    
        
        for i in range(len(s)-len(t)+1):
            diff=0
            ans=True
            for j in range(i,i+len(t)):
                right=j-i
                left=j
                if s[left]!=t[right]:
                    if t[right] in k[s[left]]:
                        continue
                    else:
                        ans=False
                        break
            if ans:
                return True
        return False