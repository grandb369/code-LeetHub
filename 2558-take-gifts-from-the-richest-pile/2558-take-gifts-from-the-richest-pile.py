from heapq import *
class Solution:
    def pickGifts(self, nums: List[int], k: int) -> int:
        temp=[]
        for i in nums:
            heappush(temp,-i)
        while k:
            cur=heappop(temp)
            cur*=-1
            cur=math.floor(cur**0.5)
            heappush(temp,-cur)
            k-=1
        return -1*sum(temp)