class Solution():
    def findNumberOfLIS(self, nums):
        n=len(nums)
        if n<2:
            return n
        count=[1 for i in range(n)] 
        dp=[0 for i in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[j]<nums[i]:
                    if dp[j]>=dp[i]:
                        dp[i]=dp[j]+1
                        count[i]=count[j]
                    elif dp[j]+1==dp[i]:
                        count[i]+=count[j]
        val=max(dp)
        return sum(j for i,j in enumerate(count)if dp[i]==val)
       