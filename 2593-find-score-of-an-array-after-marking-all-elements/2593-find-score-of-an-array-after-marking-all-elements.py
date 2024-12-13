from heapq import *
class Solution:
    def findScore(self, nums: List[int]) -> int:
        out=0
        k=collections.defaultdict(list)
        n=len(nums)
        for i in range(n-1,-1,-1):
            j=nums[i]
            k[j].append(i)
        temp=[]
        for i in k:
            heappush(temp,(i,k[i]))
        seen=set([])
        while temp:
            v,cur=heappop(temp)
            index=cur.pop()
            if index in seen:
                seen.remove(index)
            else:
                out+=v
                if index-1>=0:
                    seen.add(index-1)
                if index+1<n:
                    seen.add(index+1)
            if cur:
                heappush(temp,(v,cur))
        return out