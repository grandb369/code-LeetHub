class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort(reverse=True)
        s.sort(reverse=True)
        out=0
        while g and s:
            if s[-1]>=g[-1]:
                g.pop()
                out+=1
            s.pop()
        return out