class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        s=[len(i)for i in s.split()]
        out=0
        for i in s:
            out=i
        return out