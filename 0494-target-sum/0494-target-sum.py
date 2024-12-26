class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0
        if nums[0]==0:
            dp={0:2}
        else:
            dp={nums[0]:1,-nums[0]:1}
        for i in range(1,len(nums)):
            temp={}
            for j in dp:
                temp[j+nums[i]]=temp.get(j+nums[i],0)+dp.get(j,0)
                temp[j-nums[i]]=temp.get(j-nums[i],0)+dp.get(j,0)
            dp=temp
        print(dp)
        return dp.get(S,0)