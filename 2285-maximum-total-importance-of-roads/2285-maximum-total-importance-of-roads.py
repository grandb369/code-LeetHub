class Solution:
    def maximumImportance(self, n: int, nums: List[List[int]]) -> int:
        temp=collections.defaultdict(set)
        for u,v in nums:
            temp[u].add(v)
            temp[v].add(u)
        out={}
        key=sorted(temp.keys(),key=lambda x:len(temp[x]),reverse=True)
        for i in key:
            out[i]=n
            n-=1
        ans=0
        for u,v in nums:
            ans+=out[u]+out[v]
        return ans