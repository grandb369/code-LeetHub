class Solution:
    def rob(self, nums: List[int]) -> int:
        out=max(nums)
        if len(nums)<3:
            return out
        nums[2]+=nums[0]
        out=max(out,nums[2])
        for i in range(3,len(nums)):
            nums[i]+=max(nums[i-2],nums[i-3])
            out=max(out,nums[i])
        return out