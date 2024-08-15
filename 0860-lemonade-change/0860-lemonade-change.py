class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if not bills:
            return True
        k={
            5:0,
            10:0
        }
        for i in bills:
            if i==5:
                k[5]+=1
            elif i==10:
                if k[5]==0:
                    return False
                else:
                    k[5]-=1
                    k[10]+=1
            else:
                if k[5]==0 or (k[10]==0 and k[5]<3):
                    return False
                elif k[10]!=0:
                    k[10]-=1
                    k[5]-=1
                else:
                    k[5]-=3
        return True