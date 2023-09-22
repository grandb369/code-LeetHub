class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s=list(s)[::-1]
        for i in t:
            if s and i==s[-1]:
                s.pop()
        return len(s)==0