from heapq import *
class Solution:
    def mostBooked(self, n: int, nums: List[List[int]]) -> int:
        out=[0 for i in range(n)]
        for i in range(len(nums)):
            nums[i][1]-=nums[i][0]
        nums.sort(reverse=True)
        room=[]
        for i in range(n):
            heappush(room,i)
        fin=[]
        while nums:
            s,t=nums.pop()
            while fin:
                e,r=heappop(fin)
                if e>s:
                    heappush(fin,(e,r))
                    break
                else:
                    heappush(room,r)
            if not room:
                e,r=heappop(fin)
                out[r]+=1
                heappush(fin,(max(s,e)+t,r))
            else:
                r=heappop(room)
                out[r]+=1
                heappush(fin,(s+t,r))
        k=collections.defaultdict(list)
        for i in range(n):
            k[out[i]].append(i)
        ma=max(k.keys())
        return k[ma][0]