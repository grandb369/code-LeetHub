from heapq import *
class Solution:
    def furthestBuilding(self, h: List[int], b: int, l: int) -> int:
        temp=[]
        out=0
        for i in range(1,len(h)):
            if h[i]>h[i-1]:
                heappush(temp,h[i]-h[i-1])
            if len(temp)>l:
                b-=heappop(temp)
            if b<0:
                return i-1
        return len(h)-1