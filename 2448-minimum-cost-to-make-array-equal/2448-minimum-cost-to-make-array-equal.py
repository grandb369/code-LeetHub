class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n=len(nums)
        out=float('inf')
        l,r=min(nums),max(nums)
        if l==r:
            return 0
        while l<r:
            mid=(l+r)//2
            v1=v2=0
            for i in range(n):
                v1+=abs(mid-nums[i])*cost[i]
                v2+=abs(mid+1-nums[i])*cost[i]
            if v1>=v2:
                l=mid+1
            else:
                r=mid
            out=min(out,v1,v2)
        return out