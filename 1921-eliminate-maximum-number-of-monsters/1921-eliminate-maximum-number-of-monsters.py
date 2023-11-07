from heapq import *
class Solution:
    def eliminateMaximum(self, nums: List[int], speed: List[int]) -> int:
        temp=[]
        n=len(nums)
        for i in range(n):
            heappush(temp,nums[i]/speed[i])
        v=0
        out=0
        while temp:
            cur=heappop(temp)
            if v>=cur:
                break
            v+=1
            out+=1
        return out