class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        out=[-1,-1]
        if not nums:
            return out
        l=0
        n=len(nums)
        r=n-1
        while l<r:
            mid=(l+r)//2
            if target==nums[mid]:
                l=mid
                if target!=nums[r]:
                    r-=1
                else:
                    l=r
            elif target>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        if nums[l]==target:
            out[1]=l
        l=0
        r=n-1
        while l<r:
            mid=(l+r)//2
            if target==nums[mid]:
                r=mid
                if target!=nums[l]:
                    l+=1
                else:
                    r=l
            elif target<nums[mid]:
                r=mid-1
            else:
                l=mid+1
        if nums[l]==target:
            out[0]=l
        return out