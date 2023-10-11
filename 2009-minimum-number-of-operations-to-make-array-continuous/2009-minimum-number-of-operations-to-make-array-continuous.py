class Solution:
    def minOperations(self, num: List[int]) -> int:
        n=len(num)
        nums=sorted(set(num))
        out=n
        for i,j in enumerate(nums):
            t=j+n-1
            l=0
            r=len(nums)
            while l<r:
                mid=(l+r)//2
                if nums[mid]>t:
                    r=mid
                else:
                    l=mid+1
            out=min(out,i+n-l)
        return out