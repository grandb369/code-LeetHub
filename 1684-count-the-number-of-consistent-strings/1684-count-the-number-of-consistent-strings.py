class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        a=set(allowed)
        out=0
        for i in words:
            ans=True
            for j in set(i):
                if j not in a:
                    ans=False
                    break
            if ans:
                out+=1
        return out