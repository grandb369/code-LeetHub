from heapq import *
class Solution:
    def minimumSize(self, nums: List[int], m: int) -> int:
        if len(nums)==1:
            m+=1
            return nums[0]//m+nums[0]%m
        nums.sort()
        l=1
        r=nums[-1]
        out=nums[-1]
        n=len(nums)
        while l<r:
            val=(l+r)//2
            index=bisect.bisect_left(nums,val)
            #print(index,nums[index],val)
            c=0
            for i in range(index,n):
                if val<nums[i]:
                    c+=nums[i]//val+(1 if nums[i]%val else 0)-1
            if c<=m:
                out=min(out,val)
                r=val
            else:
                l=val+1
        return out