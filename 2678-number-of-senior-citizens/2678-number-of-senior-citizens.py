class Solution:
    def countSeniors(self, details: List[str]) -> int:
        out=0
        for i in details:
            i=i[11:13]
            if int(i)>60:
                out+=1
        return out