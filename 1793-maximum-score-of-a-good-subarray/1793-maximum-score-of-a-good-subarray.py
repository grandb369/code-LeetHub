class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        out=nums[k]
        val=out
        l=r=k
        n=len(nums)
        while l>0 and r+1<n:
            nexl=nums[l-1]
            nexr=nums[r+1]
            if nexl==nexr:
                l-=1
                r+=1
                val=min(val,nexl)
            elif nexl>nexr:
                l-=1
                val=min(val,nexl)
            else:
                r+=1
                val=min(val,nexr)
            out=max(out,val*(r-l+1))
        while l>0:
            l-=1
            val=min(val,nums[l])
            out=max(out,val*(r-l+1))
        while r+1<n:
            r+=1
            val=min(val,nums[r])
            out=max(out,val*(r-l+1))
        return out