class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<2:
            return 0
        count=0
        pre=1
        out=0
        p1=0
        for p2,i in enumerate(nums):
            if i<k:
                out+=1
                pre*=i
                while pre>=k and count>0:
                    pre//=nums[p1]
                    p1+=1
                    count-=1
                out+=count
                count+=1
            else:
                p1=p2+1
                count=0
                pre=1
        return out