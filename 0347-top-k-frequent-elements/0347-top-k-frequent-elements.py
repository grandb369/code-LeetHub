class Solution:
    def topKFrequent(self, nums: List[int], f: int) -> List[int]:
        k=collections.defaultdict(int)
        data=[set([])for i in range(len(nums)+1)]
        count=0
        for i in nums:
            if k[i]==0:
                k[i]+=1
                data[k[i]].add(i)
            else:
                data[k[i]].remove(i)
                k[i]+=1
                data[k[i]].add(i)
            count=max(k[i],count)
        out=[]
        while f>0 and count>=0:
            val=list(data[count])
            v=min(f,len(val))
            out+=val[:v]
            f-=v
            count-=1
        return out