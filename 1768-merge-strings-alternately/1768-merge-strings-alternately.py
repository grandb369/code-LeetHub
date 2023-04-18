class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1=list(word1)[::-1]
        w2=list(word2)[::-1]
        out=''
        while w1 and w2:
            out+=w1.pop()
            out+=w2.pop()
        while w1:
            out+=w1.pop()
        while w2:
            out+=w2.pop()
        return out