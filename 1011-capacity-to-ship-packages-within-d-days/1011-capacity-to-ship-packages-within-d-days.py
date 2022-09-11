class Solution:
    def shipWithinDays(self, nums: List[int], d: int) -> int:
        r=sum(nums)
        l=max(nums)
        out=r
        while l<r:
            mid=(l+r)//2
            val=0
            count=1
            for i in nums:
                if i+val<=mid:
                    val+=i
                else:
                    count+=1
                    val=i
            if count<=d:
                r=mid
            else:
                l=mid+1
        return l