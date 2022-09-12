class Solution:
    def bagOfTokensScore(self, nums: List[int], p: int) -> int:
        out=0
        i=0
        j=len(nums)-1
        nums.sort()
        val=0
        while i<=j:
            if p>=nums[i]:
                p-=nums[i]
                val+=1
                i+=1
            elif val>0:
                val-=1
                p+=nums[j]
                j-=1
            else:
                break
            out=max(out,val)
        return out