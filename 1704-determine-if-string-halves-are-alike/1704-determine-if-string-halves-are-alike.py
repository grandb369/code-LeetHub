class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        k=set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        a=0
        b=0
        for i in range(len(s)//2):
            if s[i]in k:
                a+=1
        for i in range(len(s)//2,len(s)):
            if s[i]in k:
                b+=1
        return a==b