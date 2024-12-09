from heapq import *
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        pre_max=0
        heap=[]
        events.sort()
        out=0
        for l,r,v in events:
            while heap:
                end,v2=heappop(heap)
                if end>=l:
                    heappush(heap,(end,v2))
                    break
                pre_max=max(pre_max,v2)
            out=max(out,v+pre_max)
            heappush(heap,(r,v))
        return out