class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        out=0
        temp=collections.defaultdict(int)
        su=0
        for i in range(k):
            su+=nums[i]
            temp[nums[i]]+=1
        if len(temp)==k:
            out=max(out,su)
        for i in range(k,len(nums)):
            su-=nums[i-k]
            su+=nums[i]
            temp[nums[i]]+=1
            temp[nums[i-k]]-=1
            if temp[nums[i-k]]==0:
                del temp[nums[i-k]]
            if len(temp)==k:
                out=max(out,su)
        return out