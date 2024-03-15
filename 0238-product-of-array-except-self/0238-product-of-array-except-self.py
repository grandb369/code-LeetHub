class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        out=[1 for i in range(len(nums))]
        val=1
        for i in range(len(nums)-1):
            val*=nums[i]
            out[i+1]*=val
        val=1
        for i in range(len(nums)-1,0,-1):
            val*=nums[i]
            out[i-1]*=val
        return out 