class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        k={0:-1}
        count=0
        out=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                count-=1
            if count in k:
                out=max(out,i-k[count])
            else:
                k[count]=i
        return out