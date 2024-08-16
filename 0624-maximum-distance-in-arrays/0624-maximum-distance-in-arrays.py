class Solution:
    def maxDistance(self, nums: List[List[int]]) -> int:
        n=len(nums)
        lmin=[0]*n
        lmax=[0]*n
        rmin=[0]*n
        rmax=[0]*n
        lmi=lmin[0]=nums[0][0]
        lma=lmax[0]=nums[0][-1]
        rmi=rmin[-1]=nums[-1][0]
        rma=rmax[-1]=nums[-1][-1]
        for i in range(1,n):
            l,r=nums[i][0],nums[i][-1]
            lmi=min(l,lmi)
            lma=max(r,lma)
            lmin[i],lmax[i]=lmi,lma
            
            l,r=nums[-1-i][0],nums[-1-i][-1]
            rmi=min(l,rmi)
            rma=max(r,rma)
            rmin[-1-i],rmax[-1-i]=rmi,rma
        out=0
        for i in range(n):
            l,r=nums[i][0],nums[i][-1]
            ma=float('-inf')
            mi=float('inf')
            if i-1>=0:
                ma=max(ma,lmax[i-1])
                mi=min(mi,lmin[i-1])
            if i+1<n:
                ma=max(ma,rmax[i+1])
                mi=min(mi,rmin[i+1])
            out=max(out,ma-l,r-mi)

        return out