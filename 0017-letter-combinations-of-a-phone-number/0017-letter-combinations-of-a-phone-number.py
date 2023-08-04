class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        k={str(i+2):j for i,j in enumerate(['abc','def','ghi','jkl','mno','pqrs','tuv','wxyz'])}
        out=[]
        if not digits:
            return []
        def back(temp,s,out):
            if not s:
                out.append(temp)
            else:
                cur=s[0]
                for i in k[cur]:
                    back(temp+i,s[1:],out)
        back('',digits,out)
        return out