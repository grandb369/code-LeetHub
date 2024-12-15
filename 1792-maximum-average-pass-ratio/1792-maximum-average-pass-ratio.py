from heapq import *
class Solution:
    def maxAverageRatio(self, classes: List[List[int]], q: int) -> float:
        temp=[]
        ans=[]
        for j,x in enumerate(classes):
            l,r=x
            ans.append(l/r)
            l+=1
            r+=1
            val=l/r-ans[-1]
            val*=-1
            heappush(temp,(val,j,l,r))
        for i in range(q):
            val,j,l,r=heappop(temp)
            ans[j]=l/r
            l+=1
            r+=1
            val=l/r-ans[j]
            val*=-1
            heappush(temp,(val,j,l,r))
        out=0
        for i in ans:
            out+=i
        return out/len(classes)