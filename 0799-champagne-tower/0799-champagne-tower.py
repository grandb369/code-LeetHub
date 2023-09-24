class Solution:
    def champagneTower(self, n: int, r: int, c: int) -> float:
        pre=[n]
        for i in range(1,r+1):
            cur=[max((pre[0]-1)/2,0)]
            for j in range(len(pre)-1):
                val=max(0,(pre[j]-1)/2)+max(0,(pre[j+1]-1)/2)
                cur.append(val)
            cur.append(max((pre[0]-1)/2,0))
            pre=cur
        return min(1,pre[c])