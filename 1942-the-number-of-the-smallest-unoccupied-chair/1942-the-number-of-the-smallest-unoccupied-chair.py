from heapq import *
class Solution:
    def smallestChair(self, times: List[List[int]], t: int) -> int:
        nums=[]
        for i in range(len(times)):
            nums.append([times[i][0],times[i][1],i])
        nums.sort(reverse=True)
        temp=[i for i in range(len(times))]
        heapify(temp)
        end=collections.defaultdict(list)
        i=0
        while True:
            if i in end:
                while end[i]:
                    heappush(temp,end[i].pop())
                del end[i]
            s,e,cur=nums.pop()
            if s>i:
                nums.append([s,e,cur])
                i+=1
                continue
            sit=heappop(temp)
            if cur==t:
                return sit
            end[e].append(sit)
            i+=1
        