class Solution:
    def isCircularSentence(self, s: str) -> bool:
        s=s.split()
        if s[0][0]!=s[-1][-1]:
            return False
        for i in range(1,len(s)):
            if s[i][0]!=s[i-1][-1]:
                return False
        return True