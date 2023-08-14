class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        out=[False for i in range(n+1)]
        out[0]=True
        for i in range(n+1):
            if i>=2 and nums[i-1]==nums[i-2]:
                out[i]=out[i-2]
            if i>=3:
                if nums[i-1]==nums[i-2]==nums[i-3]:
                    out[i]= out[i]or out[i-3]
                if nums[i-1]==nums[i-2]+1==nums[i-3]+2:
                    out[i]= out[i]or out[i-3]
        return out[-1]
                