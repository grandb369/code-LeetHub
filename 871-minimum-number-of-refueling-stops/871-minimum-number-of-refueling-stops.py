from heapq import *
class Solution:
    def minRefuelStops(self, t: int, e: int, nums: List[List[int]]) -> int:
        out=0
        temp=[]
        nums.sort()
        for i,j in nums:
            while e<i:
                if not temp:
                    return -1
                e-=heappop(temp)
                out+=1
            heappush(temp,-j)
        while temp and e<t:
            e-=heappop(temp)
            out+=1
        if e>=t:
            return out
        return -1