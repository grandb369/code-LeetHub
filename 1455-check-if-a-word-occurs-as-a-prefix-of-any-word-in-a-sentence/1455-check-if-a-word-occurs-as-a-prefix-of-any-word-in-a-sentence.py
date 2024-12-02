class Solution:
    def isPrefixOfWord(self, sentence: str, se: str) -> int:
        s=sentence.split()
        for i in range(len(s)):
            if se==s[i][:len(se)]:
                return i+1
        return -1