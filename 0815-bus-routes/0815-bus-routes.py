class Solution:
    def numBusesToDestination(self, nums: List[List[int]], s: int, t: int) -> int:
        if s==t:return 0
        temp=collections.defaultdict(set)
        for i,j in enumerate(nums):
            for x in j:
                temp[x].add(i)
        stack=[s]
        seen=set([s])
        out=0
        while stack:
            out+=1
            nex=set([])
            for i in stack:
                for j in temp[i]:
                    for x in nums[j]:
                        if x==t:
                            return out
                        if x not in seen:
                            seen.add(x)
                            nex.add(x)
                    nums[j]=[]
            stack=nex
        return -1