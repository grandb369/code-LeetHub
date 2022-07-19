from heapq import *
class Solution:
    def assignTasks(self, ser: List[int], ts: List[int]) -> List[int]:
        busy=[]
        wait=[]
        out=[]
        for i in range(len(ser)):
            heappush(wait,[ser[i],i,0])
        for time,t in enumerate(ts):
            while not wait or busy and busy[0][0]<=time:
                _time,wei,index=heappop(busy)
                heappush(wait, [wei,index,_time])
            wei,index,_time=heappop(wait)
            out.append(index)
            heappush(busy,[max(time,_time)+t,wei,index])
        return out