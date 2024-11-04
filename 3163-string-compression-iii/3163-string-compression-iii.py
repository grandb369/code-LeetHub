class Solution:
    def compressedString(self, word: str) -> str:
        n=len(word)
        out=''
        c=1
        for i in range(1,n):
            if word[i]!=word[i-1]:
                out+=str(c)+word[i-1]
                c=1
            elif c==9:
                out+='9'+word[i]
                c=1
            else:
                c+=1
        return out+str(c)+word[-1]