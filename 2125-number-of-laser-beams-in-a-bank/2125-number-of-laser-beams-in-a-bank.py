class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        temp=[]
        for i in bank:
            val=i.count('1')
            if val!=0:
                temp.append(val)
        out=0
        if not temp:
            return out
        pre=temp.pop()
        while temp:
            cur=temp.pop()
            out+=pre*cur
            pre=cur
        return out