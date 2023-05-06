class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        out=0
        n=len(nums)
        mod=10**9+7
        for i in range(n):
            l=i
            r=n
            v1=nums[i]
            while l<r:
                mid=(l+r)//2
                if nums[mid]+v1<=target:
                    l=mid+1
                else:
                    r=mid
            if l>=n:
                l-=1
            if nums[l]+v1>target:
                l-=1
            if l>=i:
                out+=pow(2,l-i,mod)
        return out%mod