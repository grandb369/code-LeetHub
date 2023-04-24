from heapq import *
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        temp=[]
        for i in stones:
            heappush(temp,-i)
        while len(temp)>1:
            v1=-heappop(temp)
            v2=-heappop(temp)
            val=abs(v1-v2)
            if val!=0:
                heappush(temp,-val)
        return -temp[0] if temp else 0