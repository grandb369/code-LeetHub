class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        out=0
        val=0
        vew=set(['a','e','i','o','u'])
        for i in range(k):
            if s[i]in vew:
                val+=1 
        out=val
        for i in range(k,len(s)):
            if s[i-k]in vew:
                val-=1
            if s[i] in vew:
                val+=1
            out=max(out,val)
        return out