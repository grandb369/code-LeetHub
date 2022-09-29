class Solution:
    def findClosestElements(self, nums: List[int], k: int, x: int) -> List[int]:
        out=[]
        ans=[]
        l=0
        r=n=len(nums)
        while l<r:
            mid=(l+r)//2
            if nums[mid]<x:
                l=mid+1
            else:
                r=mid
        if l==len(nums) or (l>0 and abs(nums[l-1]-x)<=abs(nums[l]-x)):
            l-=1
        if nums[l]<=x:
            ans.append(nums[l])
        else:
            out.append(nums[l])
        r=l+1
        l-=1
        for i in range(k-1):
            if l>=0 and r<n:
                if abs(nums[l]-x)<=abs(nums[r]-x):
                    ans.append(nums[l])
                    l-=1
                else:
                    out.append(nums[r])
                    r+=1
            elif l>=0:
                ans.append(nums[l])
                l-=1
            else:
                out.append(nums[r])
                r+=1
        ans.reverse()
        ans+=out
        return ans