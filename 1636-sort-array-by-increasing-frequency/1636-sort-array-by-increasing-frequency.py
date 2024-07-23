class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        k=collections.defaultdict(int)
        for i in nums:
            k[i]+=1
        count=collections.defaultdict(list)
        for i in k:
            count[k[i]].append(i)
        out=[]
        for i in sorted(count.keys()):
            for x in sorted(count[i],reverse=True):
                out+=[x for y in range(i)]
        return out